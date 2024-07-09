from django.urls import path

from myadmin.views import admin_index
from myadmin.views import user,card



urlpatterns = [

    path('', admin_index.index, name='myadmin_index'),

    path('card/', card.generate_card, name='myadmin_card'),

    #员工账号信息管理
    path('user/<int:pIndex>', user.index, name="myadmin_user_index"),#浏览信息
    path('user/add', user.add, name="myadmin_user_add"),             #加载添加表单
    path('user/insert', user.insert, name="myadmin_user_insert"),     #执行信息添加
    path('user/del/<int:uid>', user.delete, name="myadmin_user_del"),#删除信息
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"),#准备信息编辑
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"),#执行信息编辑


]