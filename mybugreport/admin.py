from django.contrib import admin
from .models import Bugtemlate
# Register your models here.

class BugtemlateAdmin(admin.ModelAdmin):
    '''
    bug模板后台
    '''
    list_display = ('user','temlatename','temcreatetime')



admin.site.register(Bugtemlate,BugtemlateAdmin)

