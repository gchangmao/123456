from django.conf.urls import url
from . import views


urlpatterns = [
    #http://127.0.0.1:8000/index/mymiddle
    url(r'^mymiddle$', views.mymiddle),
    #http://127.0.0.1:8000/index/book
    url(r'^book$', views.book),
    #http://127.0.0.1:8000/index/test_upload
    url(r'^test_upload$', views.test_upload),
    #http://127.0.0.1:8000/index/book_csv
    url(r'^book_csv$', views.book_csv)
]