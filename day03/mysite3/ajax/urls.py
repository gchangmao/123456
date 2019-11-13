from django.conf.urls import url

from . import views

urlpatterns = [
    #127.0.0.0:8000/ajax/test_load
    url(r'^test_load$',views.test_load),
    url(r'^test_load_server$',views.test_load_server),

    url(r'^test_get_server$',views.test_get_server),
    url(r'^test_get$',views.test_get),

    url(r'^test_post_server$',views.test_post_server),
    url(r'^test_post$',views.test_post),

    url(r'^test_ajax_server$',views.test_ajax_server),
    url(r'^test_ajax$',views.test_ajax),

    url(r'^test_cross_server$', views.test_cross_server),
    url(r'^test_cross$', views.test_cross),

    url(r'^test_cross_server_json$', views.test_cross_server_json),

]