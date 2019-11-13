"""amysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test_xhr/$', views.test_xhr),
    url(r'^get_xhr/$', views.get_xhr),
    url(r'^get_xhr_server/$', views.get_xhr_server),
    url(r'^user/',include('user.urls')),
    url(r'^post_xhr/$',views.post_xhr),
    url(r'^post_xhr_server/$',views.post_xhr_server),
    url(r'^test_json/$',views.test_json)

]