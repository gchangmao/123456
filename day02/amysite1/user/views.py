from django.http import HttpResponse
from django.shortcuts import render
from .models import User

# Create your views here.
def register(request):

    if request.method == 'GET':
        #拿页面
        return render(request,'register.html')
    elif request.method == 'POST':
        #处理数据
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        users = User.objects.filter(username=username)
        if users:
            return HttpResponse('当前用户以存在')
        user = User.objects.create(username=username,password=pwd,nickname=username)

        return HttpResponse('注册成功')

def check_username(request):
    #检查用户名是否已注册
    #1.获取前端传来的用户名  /user/check_username?username=xx
    username = request.GET.get('username')
    #2.检查数据库中是否有该用户名
    users = User.objects.filter(username=username)
    if users:
        # return HttpResponse('用户名已注册')
        return HttpResponse('1')
    return HttpResponse('0')

def get_user_server(request):
    #返回用户表数据
    all_users = User.objects.all()
    all_users_list = []
    for user in all_users:
        all_users_list.append(user.to_dict())
    import json
    res = json.dumps(all_users_list)
    return HttpResponse(res)









