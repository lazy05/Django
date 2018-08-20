import logging,random
from django.contrib.auth.hashers import check_password, make_password
from django.db import DatabaseError
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse,JsonResponse
# Create your views here.
def login_views(request):

    return render(request,'index1.html')

def registe_views(request):
    if request.method == 'POST':
        users = UserInfo()
        user = request.POST.get('username',None)
        upass1 = request.POST.get('userpass',None)
        upassc = make_password(upass1,'abc','pbkdf2_sha1')
        upass2 = request.POST.get('confirmpass',None)
        uemail = request.POST.get('uemail',None)
        username = UserInfo.objects.filter(uname=user)
        if len(username) > 0:
            msg = '用户已经存在'
            return render(request,'login.html',locals())
        if upass1 != upass2:
            msg = '输入密码不一致,请重新输入'
            return render(request,'registe.html',locals())
        else:
            users.uname = user
            users.upassword = upassc
            users.email = uemail
            users.save()
            msg = '注册成功'
            return render(request,'look.html',locals())
    return render(request,'registe.html',locals())


def login1_views(request):
    return render(request,'login.html')

def login_views(request):
    if request.method == "POST":
        code1 = request.POST['code1']
        code2 = request.session['code']
        user = UserInfo()
        user.uname = request.POST.get('uname')
        user.upassword = request.POST.get('upass')
        try:
            find_user = UserInfo.objects.filter(uname=user.uname)
            if len(find_user) <= 0:
                msg = '用户不存在'
                return render(request, "registe.html", locals())
            if not check_password(user.upassword, find_user[0].upassword):
                msg = '用户名密码错误'
                return render(request, "login.html",locals())
            if code1 != code2:
                msg = '验证码错误'
                return render(request,'login.html',locals())
        except DatabaseError as e:
            logging.warning(e)
        request.session['user_id'] = find_user[0].id
        request.session['user_name'] = find_user[0].uname
        msg = '登录成功'
        return render(request, "look.html",locals())
    return redirect('/user/login1')

def index_views(request):
    return render(request,'index.html')

def look_views(request):
    return render(request,'look.html')

def detail_views(request,num):
    l = [1,2,3,4,5,6,7,8,9,10]
    titlel = content.objects.filter(li=num)[0].name
    cotent = content.objects.filter(li=num)[0].content.split(' 　　')
    user1 = Commit.objects.filter(id=random.choice(l))[0].user
    matter1 = Commit.objects.filter(id=random.choice(l))[0].matter
    user2 = Commit.objects.filter(id=random.choice(l))[0].user
    matter2 = Commit.objects.filter(id=random.choice(l))[0].matter
    user3 = Commit.objects.filter(id=random.choice(l))[0].user
    matter3 = Commit.objects.filter(id=random.choice(l))[0].matter
    user4 = Commit.objects.filter(id=random.choice(l))[0].user
    matter4 = Commit.objects.filter(id=random.choice(l))[0].matter
    return render(request,'detailtest.html',locals())

def commit_views(request):
    new_commit = Commit()
    review = request.POST.get('text')
    cont_name = request.POST.get('title')
    user_id = request.session.get('user_id')
    cont_ = content.objects.filter(name=cont_name)
    user_ = UserInfo.objects.get(id=user_id)
    if len(cont_) > 0:
        new_commit.user = user_
        new_commit.title = cont_[0]
        new_commit.matter = review
        new_commit.save()
        title = content.objects.filter(li=num)[0].name
        cotent = content.objects.filter(li=num)[0].content.split(' 　　')
        return render(request,'detailtest.html',locals())
    else:
        return render(request,'look.html')

def loginout_views(request):
    try:
        if request.session['user_name']:
            del request.session['user_name']
            del request.session['user_id']
    except:
        print('清除失败')
    return render(request,'look.html')


def get_views(request):
    matter = Commit.objects.filter(id=1)
    print(matter)
    return render(request,'hh.html',locals())

def check_code(request):
    from PIL import Image,ImageDraw,ImageFont
    import random
    bgcolor = (random.randrange(50,100),random.randrange(50,100),0)
    width = 60
    height = 25
    image = Image.new('RGB',(width,height),bgcolor)
    font = ImageFont.truetype('FreeMono.ttf',24)
    draw = ImageDraw.Draw(image)
    text = '0123456789abcdefghlmnzyxABCDEFGHIJKLEWQ'
    textTemp=''
    for i in range(4):
        textTemp1 = text[random.randrange(0,len(text))]
        textTemp+=textTemp1
    request.session['code'] = textTemp
    print(textTemp)
    draw.text((0,0),textTemp,(255,255,255),font)
    import io
    buf= io.BytesIO()
    image.save(buf,'png')
    return HttpResponse(buf.getvalue(),'image/png')

def verifyTest(request):
    return render(request,'login.html')

def ajax_views(request):
    # return JsonResponse({'res':1})
    username = request.GET.get('uname')
    password = request.GET.get('upass')
    print(username)
    if username == 'smart' and password == '123':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})


