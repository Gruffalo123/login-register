from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.


def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    pass
    return render(request,'login/login.html')

def register(request):
    pass
    return render(request,'login/register.html')


#logout之后，页面重定向到'/login/'这个url，也可以重定向到别的页面
def logout(request):
    pass
    return redirect('/login/')