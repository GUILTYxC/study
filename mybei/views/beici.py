from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from mybei.models import Cet4Word, UserSettings, User

def update_user_settings(request):
    if request.method == 'POST':
        daily_new_words = request.POST.get('daily_new_words')
        last_page_visited = request.POST.get('last_page_visited')

        user_dict = request.session.get('user')
        user_id = user_dict['id']
        user = User.objects.get(id=user_id)  # 获取 User 实例
        user_settings, created = UserSettings.objects.get_or_create(user=user)
        user_settings.daily_new_words = int(daily_new_words)
        user_settings.last_page_visited = int(last_page_visited)
        user_settings.save()

        return redirect('my_beici')

def beici(request):
    user_dict = request.session.get('user')
    user_id = user_dict['id']

    user = User.objects.get(id=user_id)  # 获取 User 实例
    user_settings, created = UserSettings.objects.get_or_create(user=user)
    if created:
        user_settings.daily_new_words = 20
        user_settings.last_page_visited = 1
        user_settings.save()

    page_number = request.GET.get('page', user_settings.last_page)
    words_per_page = user_settings.daily_new_words

    words_list = Cet4Word.objects.all()
    paginator = Paginator(words_list, words_per_page)
    page_obj = paginator.get_page(page_number)

    user_settings.last_page = page_obj.number
    user_settings.save()

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'mybei/beici.html', context)
