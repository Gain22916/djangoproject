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
    url(r'test12/$', viewstest.test12),
    url(r'loginpage/$', viewstest.loginpage),
    url(r'loginpage/login$', viewstest.loginpage),
    url(r'test13/$', viewstest.ChangeStatus.as_view()),
    url(r'test14/$', viewstest.test14),
    url(r'test15/$', viewstest.ChangeStatus2.as_view()),
    url(r'test16/$', viewstest.ChangeStatus2_2.as_view()),
    url(r'test17/$', viewstest.ChangeStatus3.as_view()),
    url(r'test18/$', viewstest.ChangeStatus4.as_view()),
    url(r'test19/$', viewstest.ChangeStatus5.as_view()),
    url(r'test20/$', viewstest.ChangeStatus6.as_view()),
    url(r'test21/$', viewstest.ChangeStatus7.as_view()),
    url(r'test22/$', viewstest.ChangeStatus8.as_view()),
    url(r'test23/$', viewstest.ChangeStatus9.as_view()),
    url(r'test24/$', viewstest.ChangeStatus10.as_view()),
    url(r'test25/$', viewstest.ChangeStatus11.as_view()),
    url(r'test26/$', viewstest.ChangeStatus12.as_view()),
    url(r'test27/$', viewstest.ChangeStatus13.as_view()),
    url(r'test28/$', viewstest.ChangeStatus14.as_view()),
    url(r'test29/$', viewstest.ChangeStatus15.as_view()),
    url(r'test30/$', viewstest.ChangeStatus16.as_view()),
    url(r'test31/$', viewstest.ChangeStatus17.as_view()),
    url(r'test32/$', viewstest.ChangeStatus18.as_view()),
    url(r'test33/$', viewstest.ChangeStatus19.as_view()),
    url(r'test34/$', viewstest.ChangeStatus20.as_view()),
    url(r'test35/$', viewstest.ChangeStatus21.as_view()),
    url(r'test36/$', viewstest.ChangeStatus22.as_view()),
    url(r'test37/$', viewstest.ChangeStatus23.as_view()),
    url(r'test38/$', viewstest.ChangeStatus24.as_view()),
    url(r'test39/$', viewstest.ChangeStatus25.as_view()),
    url(r'test40/$', viewstest.ChangeStatus26.as_view()),
    url(r'test41/$', viewstest.ChangeStatus27.as_view()),
    url(r'test42/$', viewstest.ChangeStatus28.as_view()),
    url(r'test43/$', viewstest.Error_message.as_view()),
    url(r'test44/$', viewstest.ChangeMode.as_view()),
    url(r'mainpage/$', viewstest.Main_page.as_view()),
    url(r'test47/$', viewstest.SPC_001.as_view()),



]
