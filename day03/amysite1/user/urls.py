from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register$',views.register),
    url(r'^check_username$',views.check_username),
    url(r'^get_user_server$', views.get_user_server),
    url(r'^get_user$', views.get_user)
]
