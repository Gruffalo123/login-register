from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from . import models
from . import forms

def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
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
    pass
    return redirect('/login/')