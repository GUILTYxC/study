from django.http import JsonResponse
from django.shortcuts import render
from myapp.models import Cet4_year, cet4data,Stardict,Wordbook
from django.shortcuts import redirect, reverse
from django.views.decorators.http import require_POST
from myadmin.models import User

def zhuci(request):
    years = Cet4_year.objects.all().order_by('name')
    context = {'years': years}
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == "POST":
        selected_year = request.POST.get('selectedYear', None)
        selected_type = request.POST.get('selectedType', None)
        results = cet4data.objects.filter(year=selected_year, section_type=selected_type)

        # 渲染筛选结果到 HTML 字符串
        data_html = ''
        for result in results:
            data_html += f'<div class="reading-material"><h2>{result.year} - {result.section_type}</h2>'
            data_html += '<div class="content-panel"><div class="text-content">'
            for paragraph in result.text_content.split('\\n'):
                data_html += '<p>' + ' '.join(
                    [f'<span class="word">{word}</span>' for word in paragraph.split()]) + '</p>'
            data_html += '</div></div>'

            # 根据不同的题型处理问题数据
            if '阅读passage1' or '阅读passage2' in selected_type:
                # 处理阅读题型的问题数据
                for i in range(1, 21):
                    question_data = getattr(result, f'question_{i}', None)
                    if question_data:
                        parts = question_data.split('\\n', 1)
                        if len(parts) > 1:
                            question_text, options_part = parts
                            options = options_part.split('\\n')
                            data_html += f'<div class="question"><div class="question-text"> '
                            data_html += ' '.join(
                                [f'<span class="word">{word}</span>' for word in question_text.split()]) + '</div>'
                            data_html += '<div class="options"><ul>'
                            for option in options:
                                data_html += '<li>' + ' '.join(
                                    [f'<span class="word">{word}</span>' for word in option.split()]) + '</li>'
                            data_html += '</ul></div></div>'
            elif selected_type == '完型填空':
                # 处理完型填空题型的问题数据
                for i in range(1, 21):
                    question_data = getattr(result, f'question_{i}', None)
                    if question_data:
                        parts = question_data.split('\\n', 1)
                        if len(parts) > 1:
                            question_text, options_part = parts
                            options = options_part.split('\\n')
                            data_html += '<div class="cloze-question">'
                            data_html += f'<span class="cloze-question-text"> ' + ' '.join(
                                [f'<span class="word">{word}</span>' for word in question_text.split()]) + '</span>'
                            for option in options:
                                data_html += f'<span class="cloze-option"> ' + ' '.join(
                                    [f'<span class="word">{word}</span>' for word in option.split()]) + '</span>'
                            data_html += '</div>'
            elif selected_type == '翻译':
                # 处理翻译题型的问题数据
                for i in range(1, 21):  # 假设有 5 个翻译问题
                    question_data = getattr(result, f'question_{i}', None)
                    if question_data:
                        data_html += '<div class="translation-question">'
                        data_html += '<div class="translation-text">'
                        data_html += ' '.join([f'<span class="word">{word}</span>' for word in question_data.split()])
                        data_html += '</div></div>'
            elif selected_type == '段落匹配':
                # 处理翻译题型的问题数据
                for i in range(1, 21):  # 假设有 5 个翻译问题
                    question_data = getattr(result, f'question_{i}', None)
                    if question_data:
                        data_html += '<div class="translation-question">'
                        data_html += '<div class="translation-text">'
                        data_html += ' '.join([f'<span class="word">{word}</span>' for word in question_data.split()])
                        data_html += '</div></div>'

            data_html += '</div></div>'
        return JsonResponse({'data': data_html})
    return render(request, 'myapp/zhuci4.html', context)


def translate_word(request):
    word = request.GET.get('word', '').lower()
    try:
        stardict_entry = Stardict.objects.get(word=word)
        translation = stardict_entry.translation
        phonetic = stardict_entry.phonetic
    except Stardict.DoesNotExist:
        translation = 'Translation not found'
        phonetic = ''
    return JsonResponse({'word': word, 'translation': translation, 'phonetic': phonetic})


@require_POST
def add_to_wordbook(request):
    if 'user' not in request.session:
        return JsonResponse({'status': 'error', 'message': '请先登录'})

    user_id = request.session['user']['id']
    word = request.POST.get('word')
    phonetic = request.POST.get('phonetic')
    translation = request.POST.get('translation')

    try:
        user = User.objects.get(id=user_id)
        Wordbook.objects.create(
            user=user,
            word=word,
            phonetic=phonetic,
            translation=translation
        )
        return JsonResponse({'status': 'success', 'message': '已添加到单词本'})
    except User.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': '用户不存在'})
