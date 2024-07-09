from django.urls import path

from myapp.views import zhuci6, zhuci4, zhuci, index, home, chat, wordbook

urlpatterns = [
    path('', index.index, name='my_index'),
    path('home/', home.home, name='my_home'),

    path('activate_card/', index.activate_card, name='activate_card'),

    # 用户登录、退出路由
    path('login/', index.login, name='my_login'),  # 加载登录表单
    path('dologin/', index.dologin, name='my_dologin'),  # 执行登录
    path('logout/', index.logout, name='my_logout'),  # 退出
    path('register/', index.register, name='my_register'),  # 注册
    path('verify/', index.verify, name="my_verify"),  # 验证码

    path('zhuci/', zhuci.zhuci, name='my_zhuci'),  # 指向首页的视图
    path('translate/', zhuci.translate_word, name='translate_word'),
    path('add_to_wordbook/', zhuci.add_to_wordbook, name='add_to_wordbook'),

path('zhuci4/', zhuci4.zhuci, name='my_zhuci4'),  # 指向首页的视图
    path('translate4/', zhuci4.translate_word, name='translate_word4'),
    path('add_to_wordbook4/', zhuci4.add_to_wordbook, name='add_to_wordbook4'),

path('zhuci6/', zhuci6.zhuci, name='my_zhuci6'),  # 指向首页的视图
    path('translate6/', zhuci6.translate_word, name='translate_word6'),
    path('add_to_wordbook6/', zhuci6.add_to_wordbook, name='add_to_wordbook6'),

    path('chat_home/', chat.chat_home, name='chat_home'),
    path('ask_chatgpt/', chat.chat_with_gpt, name='ask_chatgpt'),


    path('wordbook/', wordbook.wordbook, name='my_wordbook'),
    path('update_user_settingswordbook/', wordbook.update_user_settings_wordbook,
         name='my_update_user_settingswordbook'),
    path('export_wordbook_to_excel/', wordbook.export_wordbook_to_excel, name='export_wordbook_to_excel'),

]
