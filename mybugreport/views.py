from django.shortcuts import render

# Create your views here.


def addbug(request):
    '''
    新增bug
    :param request:
    :return:
    '''

    return render(request,"add_bug.html")

def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    return render(request,"index.html")



def addproject(request):
    '''
    新增项目
    :param request:
    :return:
    '''
    return render(request,"addproject.html")



def projectdetail(request):
    '''
    项目详情
    '''

    return render(request,"projectdetail.html")