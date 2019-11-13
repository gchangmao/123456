import csv
import os

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
# Create your views here.
def mymiddle(request):

    print('---views start---')

    return HttpResponse('---test is ok---')

def book(request):
    #带分页的book列表页
    all_books = Book.objects.all()
    #初始化paginator对象
    paginator = Paginator(all_books, 2)

    #http://127.0.0.1:8000/index/book?page=1
    current_page = request.GET.get('page', 1)
    page = paginator.page(current_page)
    return render(request, 'index/book.html', locals())


def test_upload(request):
    #上传文件
    if request.method == 'GET':
        return render(request, 'index/test_upload.html')

    elif request.method == 'POST':
        myfile = request.FILES['myfile']
        file_path = os.path.join(settings.MEDIA_ROOT,myfile.name)

        with open(file_path, 'wb') as f:
            data = myfile.file.read()
            f.write(data)

        return HttpResponse('上传成功')

def book_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Dispostion'] = 'attachment;filename=book.csv'

    #带分页的book列表页
    all_books = Book.objects.all()
    #初始化paginator对象
    paginator = Paginator(all_books, 2)

    #http://127.0.0.1:8000/index/book?page=1
    current_page = request.GET.get('page', 1)
    page = paginator.page(current_page)

    writer = csv.writer(response)
    writer.writerow(['id', 'title'])
    for book in page:
        writer.writerow([book.id, book.title])
    return response






















