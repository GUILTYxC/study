from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from myapp.models import Wordbook, UserSettingsWordbook, User
from django.http import HttpResponse
from openpyxl import Workbook
from django.utils import timezone


def update_user_settings_wordbook(request):
    if request.method == 'POST':
        daily_new_words = request.POST.get('daily_new_words')
        last_page_visited = request.POST.get('last_page_visited')

        user_dict = request.session.get('user')
        user_id = user_dict['id']
        user = User.objects.get(id=user_id)  # 获取 User 实例
        user_settings, created = UserSettingsWordbook.objects.get_or_create(user=user)
        user_settings.daily_new_words = int(daily_new_words)
        user_settings.last_page_visited = int(last_page_visited)
        user_settings.save()

        return redirect('my_wordbook')

def wordbook(request):
    user_dict = request.session.get('user')
    user_id = user_dict['id']

    user = User.objects.get(id=user_id)  # 获取 User 实例
    user_settings, created = UserSettingsWordbook.objects.get_or_create(user=user)
    if created:
        user_settings.daily_new_words = 20
        user_settings.last_page_visited = 1
        user_settings.save()

    page_number = request.GET.get('page', user_settings.last_page)
    words_per_page = user_settings.daily_new_words

    words_list = Wordbook.objects.filter(user_id=user_id).order_by('added_at')
    paginator = Paginator(words_list, words_per_page)
    page_obj = paginator.get_page(page_number)

    user_settings.last_page = page_obj.number
    user_settings.save()

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'myapp/wordbook.html', context)



def export_wordbook_to_excel(request):
    if 'user' not in request.session:
        return HttpResponse("请先登录", status=401)

    user_info = request.session['user']
    user_id = user_info['id']
    words = Wordbook.objects.filter(user_id=user_id).order_by('added_at')

    wb = Workbook()
    ws = wb.active
    ws.append(['单词', '音标', '翻译'])

    for word in words:
        # Convert datetime to timezone-naive in the local timezone

        ws.append([word.word, word.phonetic, word.translation])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="wordbook.xlsx"'
    wb.save(response)

    return response

