# -*- coding: utf-8 -*-
__author__ = "langtuteng" 
from django import forms

class LoginForm(forms.Form):
    '''
    登录表单
    '''

    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入用户名称"}),error_messages={"required": "用户名不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"请输入登录密码"}),error_messages={"required": "密码不能为空",})