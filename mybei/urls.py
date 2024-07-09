from django.urls import path

from mybei.views import beici

urlpatterns = [

    path('beici/', beici.beici, name='my_beici'),
    path('update_user_settings/', beici.update_user_settings, name='my_update_user_settings'),

]
