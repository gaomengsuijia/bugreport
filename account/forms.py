# -*- coding: utf-8 -*-
__author__ = "langtuteng" 
from django import forms
from django.contrib.auth.models import User
from mybugreport.models import Userprofile
class LoginForm(forms.Form):
    '''
    登录表单
    '''

    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入用户名称"}),error_messages={"required": "用户名不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"请输入登录密码"}),error_messages={"required": "密码不能为空",})


class RegisterForm(forms.ModelForm):
    '''
    注册表单
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入登录名称"}),error_messages={"required": "账号不能为空",})
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"请输入邮箱"}),error_messages={"required": "邮箱不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"请输入登录密码"}),error_messages={"required": "密码不能为空",})
    conformpassword = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"请再次确认密码"}),error_messages={"required": "密码不能为空",})

    class Meta:
        model = User#表单数据将插入这个模型中
        fields =('username','email') #需要插入的字段
    def clean_conformpassword(self):
        cd = self.cleaned_data
        if cd['password'] != cd['conformpassword']:
            raise forms.ValidationError("passwords do not match")
        return cd['conformpassword']

class UserProfileForm(forms.ModelForm):
    '''
    用户注册新增的表1的表单
    '''
    birth = forms.DateField(widget=forms.DateTimeInput(attrs={"class":"form-control","placeholder":"请输入你的生日"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入你的生日"}))
    class Meta:
        model = Userprofile
        fields = ('birth','phone')
