
from django.utils import timezone
import pytz



from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from myadmin.models import User,Card
from django.contrib import messages
import hashlib
import random

from myapp.form import CardActivationForm


def index(request):
    # 默认信息，如果没有激活的卡或未登录
    remark = "真题通"

    if 'user' in request.session:
        user_id = request.session['user']['id']
        user = User.objects.get(id=user_id)
        # 获取最后一次激活的卡
        last_activated_card = user.cards.filter(is_activated=True).order_by('-activated_at').first()

        if last_activated_card:
            remark = last_activated_card.remark or "激活的卡没有备注信息。"

    return render(request, "myapp/index.html", {'remark': remark})


def login(request):
    '''加载登录页面'''
    return render(request,"myapp/login.html")

def dologin(request):
    '''执行登录'''
    try:
        if request.POST['code'] != request.session['verifycode']:
            context = {"info": "验证码错误！"}
            return render(request, "myapp/login.html", context)

        # 根据登录账号获取用户信息
        user = User.objects.get(username=request.POST['username'])
        # 获取密码并进行md5加密
        md5 = hashlib.md5()
        s = request.POST['pass'] + user.password_salt
        md5.update(s.encode('utf-8'))

        # 校验密码是否正确
        if user.password_hash == md5.hexdigest():
            # 根据用户状态设置会话
            if user.status == 1:
                request.session['user'] = user.toDict()

                # 检查是否至少有一个激活且未过期的卡密
                active_and_not_expired = any(
                    not card.is_expired() for card in user.cards.filter(is_activated=True)
                )

                # 如果至少有一个卡密是激活且未过期的，或用户没有任何卡密，则跳转到主页
                if active_and_not_expired or not user.cards.exists():
                    return redirect(reverse('my_index'))
                else:
                    # 否则，跳转到激活卡密页面
                    return redirect(reverse('activate_card'))

            elif user.status == 6:
                request.session['adminuser'] = user.toDict()
                return redirect(reverse('myadmin_index'))
            else:
                context = {"info": "无效的用户状态！"}
        else:
            context = {"info": "登录密码错误！"}
    except User.DoesNotExist:
        context = {"info": "登录账号不存在！"}
    except Exception as err:
        print(err)
        context = {"info": "发生未知错误，请联系管理员！"}

    return render(request, "myapp/login.html", context)





def logout(request):
    '''执行退出'''
    if 'adminuser' in request.session:

        del request.session['adminuser']
    elif 'user' in request.session:

        del request.session['user']

    return redirect(reverse('my_login'))



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')  # 获取昵称
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, '两次输入的密码不一致！')
            return redirect('my_register')

        try:
            # 获取密码并进行md5加密
            md5 = hashlib.md5()
            n = random.randint(100000, 999999)
            s = password + str(n)
            md5.update(s.encode('utf-8'))
            password_hash = md5.hexdigest()
            password_salt = n

            user = User.objects.create(
                username=username,
                nickname=nickname,  # 保存昵称
                password_hash=password_hash,
                password_salt=password_salt,
                status=1
            )
            user.save()
            messages.success(request, '注册成功！')
            return redirect('my_login')
        except Exception as e:
            messages.error(request, '注册失败：' + str(e))
            return redirect('my_register')
    else:
        return render(request, 'myapp/register.html')


def verify(request):
    #引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定义变量，用于画面的背景色、宽、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (242,164,247)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    #str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    str1 = '0123456789'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/Arial.ttf', 21)
    #font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, -3), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, -3), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, -3), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, -3), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def activate_card(request):
    if 'user' not in request.session:
        # 如果用户未登录，重定向到登录页面
        return redirect(reverse('my_login'))
    if request.method == 'POST':
        form = CardActivationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                # 尝试获取卡密
                card = Card.objects.get(code=code)

                # 检查卡密是否已被激活
                if card.is_activated:
                    messages.error(request, '该卡密已被使用。')
                    return render(request, 'myapp/activate_card.html', {'form': form})

                # 检查用户是否已登录
                if 'user' in request.session:
                    user_info = request.session['user']
                    user = User.objects.get(id=user_info['id'])
                    card.is_activated = True
                    card.activated_at = timezone.now()
                    card.user = user
                    card.save()
                    messages.success(request, '卡密激活成功！')
                    return redirect(reverse('my_index'))  # 重定向到主页
                else:
                    messages.error(request, '请先登录再激活卡密。')
            except Card.DoesNotExist:
                # 如果未找到卡密，显示错误消息
                messages.error(request, '无效的卡密。')

        return render(request, 'myapp/activate_card.html', {'form': form})
    else:
        form = CardActivationForm()

    return render(request, 'myapp/activate_card.html', {'form': form})













