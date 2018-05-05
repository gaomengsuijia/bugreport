from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Bugtemlate(models.Model):
    '''
    漏洞模板
    '''
    user = models.ForeignKey(User)
    temlatename = models.CharField(max_length=50)
    temcreatetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "bugtemplate {}".format(self.temlatename)



class Bug(models.Model):
    '''
    漏洞表
    '''
    project = models.ForeignKey("Project")
    user = models.ForeignKey(User)
    bug_name = models.CharField(max_length=100)
    bug_leval = models.CharField(max_length=25)
    bug_createtime = models.DateTimeField(auto_now_add=True)
    bug_content = models.TextField(max_length=2000)
    is_del = models.BooleanField()

    def __str__(self):
        return "bug {}".format(self.bug_name)

class Userprofile(models.Model):
    '''
    用户表
    '''
    user = models.OneToOneField(User,unique=True)
    birth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)


class Project(models.Model):
    '''
    项目表
    '''
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    projectleader = models.CharField(max_length=50)
    createtime = models.DateTimeField(auto_now_add=True)
    projecttime = models.DateTimeField()
    is_del = models.BooleanField(default=0)#1是删除，0是未删除

    def __str__(self):
        return 'project {}'.format(self.name)

