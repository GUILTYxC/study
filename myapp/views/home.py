from django.shortcuts import render
from myadmin.models import Card, User
from django.utils import timezone
from datetime import timedelta

def home(request):
    user_info = request.session.get('user', None)
    longest_remaining_days = None
    if user_info:
        user = User.objects.get(id=user_info['id'])
        user_nickname = user.nickname

        # 找到未过期时间最长的卡密
        longest_expiration_date = None
        for card in Card.objects.filter(user=user, is_activated=True):
            if not card.is_expired():
                expiration_date = card.activated_at + timedelta(days=card.duration)
                if longest_expiration_date is None or expiration_date > longest_expiration_date:
                    longest_expiration_date = expiration_date

        # 计算剩余天数
        if longest_expiration_date:
            now = timezone.now()
            longest_remaining_days = (longest_expiration_date - now).days

    else:
        # 如果用户未登录
        user_nickname = '游客'

    context = {
        'user_nickname': user_nickname,
        'remaining_days': longest_remaining_days,
    }

    return render(request, "myapp/home.html", context)
