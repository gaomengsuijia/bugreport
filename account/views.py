from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from account.forms import LoginForm,RegisterForm,UserProfileForm
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
    if request.method == "POST":
        print(request.POST)
        user_form = RegisterForm(request.POST)
        userpro_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userpro_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userpro_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse("register success")
        else:
            return HttpResponse("register fail")
    else:
        user_form = RegisterForm()
        userpro_form = UserProfileForm()
        return render(request,'mybuggreport/register.html',{"form":user_form,"user_form":userpro_form})