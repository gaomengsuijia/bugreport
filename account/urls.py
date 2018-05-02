# -*- coding: utf-8 -*-
__author__ = "langtuteng"

from django.conf.urls import url
from . import views
from django.conf import settings
urlpatterns = [
    url(r'^login/$', views.userlogin,name="userlogin"),
    url(r'^register/$',views.register,name="register"),
    url(r'^userlogout/$',views.userlogout,name="userlogout"),
]
