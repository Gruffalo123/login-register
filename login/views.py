from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from . import models

def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #此条message异常
        message = 'please check your input message'
        if username.strip() and password:
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
            except :
                message = 'user dose not exist'
                return render(request, 'login/login.html', {'message': message})

            if user.password == password:
                print(username, password)
                return redirect('/index/')
            else:
                message = 'wrong password'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')

def register(request):
    pass
    return render(request,'login/register.html')


#logout之后，页面重定向到'/login/'这个url，也可以重定向到别的页面
def logout(request):
    pass
    return redirect('/login/')