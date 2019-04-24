from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from . import models
from . import forms

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

            if user.password == password:
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
    pass
    return render(request,'login/register.html')


#logout之后，页面重定向到'/login/'这个url，也可以重定向到别的页面
def logout(request):
    #如果本来就未登录，也就没有登出一说
    if not request.sessoion.get('is_login',None):
        return redirect('/login/')
    request.session.flush()
    #或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect('/login/')

# flush()方法是比较安全的一种做法，而且一次性将session中的所有内容全部清空，确保不留后患。但也有不好的地方，那就是如果你在session中夹带了一点‘私货’，会被一并删除，这一点一定要注意