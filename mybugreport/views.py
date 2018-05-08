from django.shortcuts import render,HttpResponse
from .forms import AddprojectForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from mybugreport.models import Bug,Bugtemlate,Project
from django.db.models import ObjectDoesNotExist
from django.contrib.auth.models import User
# Create your views here.

def projectdetail(request,project_id):
    '''
    项目详情
    :param request:
    :return:
    '''

    try:
        print(project_id)
        project = Project.objects.get(id=project_id)
        if project.is_del != 1:
            print(project_id)
            bugs = Bug.objects.filter(project_id=project_id)
            return render(request, 'mybuggreport/projectdetail.html',{"projectid":project_id,"bugs":bugs})
    except ObjectDoesNotExist as e:
        return HttpResponse("4")



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


@csrf_exempt
def addbug(request,project_id):
    '''
    新增bug
    :param request:
    :return:
    '''
    if request.method == "POST":
        try:
            print(project_id)
            project =  Project.objects.get(id=int(project_id))
            print(project)
            try:
                print(request.POST)
                bug_name = request.POST['bug_name']
                bug_leval = request.POST['bug_leval']
                bugtemlate = request.POST['bugtemlate']
                bug_content = request.POST['bug_content']
                user = request.user
                bugtemlate = Bugtemlate.objects.get(id=bugtemlate)
                newBug = Bug.objects.create(bug_name=bug_name, bug_leval=bug_leval, bug_content=bug_content,bugtemlate=bugtemlate,user=user,project=project)
                newBug.save()
                print("保存成功")
                return HttpResponse("1")
            except Exception as e:
                raise Exception()
                return HttpResponse('3')
        except ObjectDoesNotExist as e:
            return HttpResponse("2")


    if request.method == "GET":

        # 查询出所有的漏洞模板
        bugtems = Bugtemlate.objects.all()
        return render(request,"mybuggreport/add_bug.html",{"bugtems":bugtems})

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
