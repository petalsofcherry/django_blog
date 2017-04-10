"""my_django_blog URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.index, name='home'),
    url(r'^blog/(?P<blog_id>\d+)/$', blog_views.each_blog, name='blog'),
    url(r'^edit/(?P<blog_id>\d+)/$', blog_views.edit, name='editBlog'),
    url(r'^delete/(?P<blog_id>\d+)/$', blog_views.delete, name='delete'),
    url(r'^admin/', admin.site.urls),
]
