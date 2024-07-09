from django.shortcuts import redirect
from django.urls import reverse
import re
from myadmin.models import User, Card
from django.core.exceptions import ObjectDoesNotExist

class AppMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        allowed_paths = [
            reverse('my_login'), reverse('my_dologin'), reverse('my_logout'),
            reverse('my_register'), reverse('my_verify'), reverse('my_index'),
            reverse('my_home'), reverse('activate_card')
        ]
        restricted_paths = [reverse('chat_home'), reverse('ask_chatgpt')]

        if re.match(r"^/myadmin", path):
            if "adminuser" not in request.session:
                return redirect(reverse('my_login'))
        else:
            user_info = request.session.get('user', None)
            if user_info:
                try:
                    user = User.objects.get(id=user_info['id'])
                    if path in restricted_paths:
                        ai_active = any(card.ai_activated and not card.is_expired() for card in user.cards.all())
                        if not ai_active:
                            return redirect(reverse('activate_card'))
                    elif not any(card.is_activated and not card.is_expired() for card in user.cards.all()) and path not in allowed_paths:
                        return redirect(reverse('activate_card'))
                except ObjectDoesNotExist:
                    del request.session['user']
                    return redirect(reverse('my_login'))
            elif path not in allowed_paths:
                return redirect(reverse('my_login'))

        response = self.get_response(request)
        return response
