from .models import Project
from django import forms


class AddprojectForm(forms.ModelForm):
    '''
    添加项目表单
    '''

    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入项目名称"}),error_messages={"required": "项目名称不能为空",})
    projecttime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control","placeholder":"请输入项目时间"}),error_messages={"required": "项目时间不能为空",})
    projectleader = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"请输入项目负责人"}),error_messages={"required": "负责人不能为空",})

    class Meta:
        model = Project
        fields = ('name','projecttime','projectleader')