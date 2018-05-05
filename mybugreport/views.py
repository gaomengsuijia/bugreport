from django.shortcuts import render,HttpResponse
from .forms import AddprojectForm
from django.contrib.auth.decorators import login_required
from mybugreport.models import Project
from mybugreport.models import Bug
# Create your views here.

def projectdetail(request,project_id):
    '''
    项目详情
    :param request:
    :return:
    '''
    try:
        project = Project.objects.get(id=project_id)
        if project.is_del != 1:
            return render(request, 'mybuggreport/projectdetail.html')
    except Exception as e:
        return HttpResponse("5")



@login_required(login_url="/account/login")
def delproject(request):
    '''
    删除项目
    :param request:
    :return:
    '''
    if request.user == "":
        return HttpResponse("3")
    if request.method == "POST":
        project_id = request.POST["project_id"]
        if project_id == "":
            HttpResponse("id is null")
        else:
            try:
                project = Project.objects.get(id=project_id)
                if project.is_del !=1:
                    project.is_del = 1
                    project.save()
                else:
                    return HttpResponse("4")
                return HttpResponse('1')

            except Exception as e:
                return HttpResponse('2')
    else:
        return HttpResponse("method erro")



def addbug(request):
    '''
    新增bug
    :param request:
    :return:
    '''

    return render(request,"mybuggreport/add_bug.html")

def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    try:
        projects = Project.objects.filter(is_del=0)
        return render(request, "mybuggreport/index.html", {"projects": projects})
    except Exception as e:
        raise Exception("查询失败")


@login_required(login_url="/account/login")
def addproject(request):
    '''
    新增项目
    :param request:
    :return:
    '''
    if request.method == "POST":
        project_form = AddprojectForm(request.POST)
        if project_form.is_valid():
            try:
                new_project = project_form.save(commit=False)
                new_project.user = request.user
                new_project.save()
                return HttpResponse("1")
            except Exception as e:
                raise Exception("保存数据失败")
        else:
            return HttpResponse("2")
    else:
        project_form = AddprojectForm()
        return render(request,"mybuggreport/addproject.html",{'project_form':project_form})
