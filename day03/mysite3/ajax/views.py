import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.


def test_load(request):

    return render(request,'test_load.html')

def test_load_server(request):

    return render(request,'test_load_server.html')

def test_get(request):

    return render(request,'test_get.html')

def test_get_server(request):

    return JsonResponse({'username':'guoxiaonao'})

def test_post(request):
    return render(request,'test_post.html')


def test_post_server(request):
    username = request.POST.get('username')
    msg = 'name is %s'%(username)
    d = {'msg':msg}
    return JsonResponse(d)

def test_ajax(request):
    return render(request,'test_ajax.html')

def test_ajax_server(request):
    import time
    time.sleep(3)

    return JsonResponse({'msg':'hahaha'})
def test_cross(request):

    return render(request,'test_cross.html')

def test_cross_server(request):
    #处理跨域请求
    func= request.GET.get('callback')
    return HttpResponse(func + "('wo kua chu kai le  ')")

def test_cross_server_json(request):
    func = request.GET.get('callback')
    d = {'name':'guoxiaonao','age':18}
    return HttpResponse( func + "(" + json.dumps(d) + ")")
