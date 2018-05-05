"""bugreport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from mybugreport import views as mybugreport_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mybugreport_views.index,name="index"),
    url(r'^addproject/$', mybugreport_views.addproject,name="addproject"),
    url(r'^projectdetail/(\d+)/$', mybugreport_views.projectdetail,name="projectdetail"),
    url(r'^addbug/(\d+)/(\d+)/$', mybugreport_views.addbug,name="addbug"),
    url(r'^delproject/$', mybugreport_views.delproject,name="delproject"),
    url(r'^account/',include('account.urls',namespace='account',app_name='account')),
    ]
