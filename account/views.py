from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from account.forms import LoginForm
# Create your views here.
from django.contrib.auth import authenticate,login
from django.contrib.auth import views


def userlogout(request):
    '''
    用户退出
    :param request:
    :return:
    '''
    views.logout(request)
    return HttpResponseRedirect("/")

def userlogin(request):
    '''
    用户登录
    :param request:
    :return:
    '''
    if request.method == "POST":
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            cd = loginform.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("login fail")
        return HttpResponse("invaild login")
    if request.method == "GET":
        loginform = LoginForm()
        return render(request,'mybuggreport/login.html',{'form':loginform})



def register(request):
    '''
    注册
    :param request:
    :return:
    '''
    return render(request,'mybuggreport/register.html')