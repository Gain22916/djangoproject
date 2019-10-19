"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from admin_management import views
from example import viewstest



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'my_index/$', views.index),
    url(r'line/$', views.line),
    url(r'test/$', viewstest.test),
    url(r'test1/$', viewstest.test1),
    url(r'test2/$', viewstest.Homeview.as_view()),
    url(r'test3/$', viewstest.test3),
    url(r'test4/$', viewstest.test4),
    path('accounts/', include('example.urls')),
    url(r'test6/$', viewstest.test6),
    path('account/', include('django.contrib.auth.urls')),
    url(r'test8/$', viewstest.test8),
    url(r'test9/$', viewstest.Linetest.as_view()),
    url(r'test10/$', viewstest.test10),
    url(r'test11/$', viewstest.test11),
    url(r'loginpage/$', viewstest.loginpage),
]
