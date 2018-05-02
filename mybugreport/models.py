from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userprofile(models.Model):
    '''
    用户表
    '''
    user = models.OneToOneField(User,unique=True)
    birth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

