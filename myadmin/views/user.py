from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime
from django.utils import timezone

import pytz
import random

from myadmin.models import User


def index(request,pIndex=1):
    umod = User.objects
    mywhere = []
    ulist = umod.filter(status__lt=9)

    kw = request.GET.get("keyword", None)
    if kw:
        # 查询员工账号或昵称中只要含有关键字的都可以
        ulist = ulist.filter(Q(username__contains=kw) | Q(nickname__contains=kw))
        mywhere.append("keyword=" + kw)



    pIndex = int(pIndex)
    page = Paginator(ulist,5)
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1

    list2 = page.page(pIndex)
    plist = page.page_range
    context = {
        "userlist": list2,
        'plist':plist,
        'pIndex':pIndex,
        'maxpages':maxpages,
        'mywhere':mywhere
    }
    return render(request, "myadmin/user/index.html", context)

def add(request):
    return render(request,"myadmin/user/add.html")

def insert(request):
    try:
        ob = User()
        ob.username = request.POST['username']
        ob.nickname = request.POST['nickname']
        # 获取密码并md5
        import hashlib
        md5 = hashlib.md5()
        n = random.randint(100000, 999999)
        s = request.POST['password'] + str(n)
        md5.update(s.encode('utf-8'))
        ob.password_hash = md5.hexdigest()
        ob.password_salt = n
        ob.status = 1
        ob.create_at = timezone.now()  # 使用 timezone.now()
        ob.update_at = timezone.now()  # 使用 timezone.now()
        ob.save()
        context = {"info": "添加成功！"}
    except Exception as err:
        print(err)
        context = {"info": "添加失败"}
    return render(request, "myadmin/info.html", context)

def delete(request,uid):
    '''删除信息'''
    try:
        ob = User.objects.get(id=uid)
        ob.status = 9
        ob.update_at = timezone.now()  # 使用 timezone.now()
        ob.save()
        context={"info":"删除成功！"}
    except Exception as err:
        print(err)
        context={"info":"删除失败"}

    return  render(request,"myadmin/info.html",context)


def edit(request,uid):
    '''加载编辑信息页面'''
    try:
        ob = User.objects.get(id=uid)
        context={"user":ob}
        return render(request,"myadmin/user/edit.html",context)
    except Exception as err:
        context={"info":"没有找到要修改的信息！"}
        return render(request,"myadmin/info.html",context)

def update(request,uid):
    '''执行编辑信息'''
    try:
        ob = User.objects.get(id=uid)
        ob.nickname = request.POST['nickname']
        ob.status = request.POST['status']
        ob.update_at = timezone.now()  # 使用 timezone.now()
        ob.save()
        context={"info":"修改成功！"}
    except Exception as err:
        print(err)
        context={"info":"修改失败"}
    return render(request,"myadmin/info.html",context)

