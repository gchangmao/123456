from django.http import HttpResponse
from django.shortcuts import render

def test_xhr(request):

    return render(request, 'test_xhr.html')

def get_xhr(request):

    return render(request, 'get_xhr.html')

def get_xhr_server(request):

    return HttpResponse('This is ajax')

