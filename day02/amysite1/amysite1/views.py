from django.http import HttpResponse
from django.shortcuts import render

def test_xhr(request):

    return render(request, 'test_xhr.html')

def get_xhr(request):

    return render(request, 'get_xhr.html')

def get_xhr_server(request):

    if 'param' in request.GET.keys():
        param = request.GET['param']
        html = 'Your param is %s'%(param)
        return HttpResponse(html)
    return HttpResponse('This is ajax')


def post_xhr(request):
    return render(request,'post_xhr.html')

def post_xhr_server(request):
    return HttpResponse('POST IS OK')


def test_json(request):

    return render(request,'test_json.html')

