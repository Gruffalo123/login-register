from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from . import models
from . import forms
import hashlib


def hash_code(s,salt='gruffalo'):#加盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode()) #update方法只接收bytes类型
    return h.hexdigest()


def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    #不允许重复登录
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        #此条message异常
        message = 'please check your input message'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = 'user dose not exist'
                return render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                # print(username, password)
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = 'wrong password'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html',locals())

def register(request):
    if request.session.get('is_login',None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "please check your input message"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = 'different password!'
                return render(request,'login/register.html',locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = 'user is already exist!'
                    return render(request,'login/register.html',locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = 'email has been registered'
                    return render(request,'login/register.html',locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request,'login/register.html',locals())

    register_form = forms.RegisterForm()
    return render(request,'login/register.html')


#logout之后，页面重定向到'/login/'这个url，也可以重定向到别的页面
def logout(request):
    #如果本来就未登录，也就没有登出一说
    if not request.session.get('is_login',None):
        return redirect('/login/')
    request.session.flush()
    #或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect('/login/')

# flush()方法是比较安全的一种做法，而且一次性将session中的所有内容全部清空，确保不留后患。但也有不好的地方，那就是如果你在session中夹带了一点‘私货’，会被一并删除，这一点一定要注意