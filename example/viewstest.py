from django.shortcuts import render, redirect
from django.template import loader
from .models import Simple
from django.http import HttpResponse
from example.forms import HomeForm
from django.views import View
import requests
from admin_management import LineAPI
from example.models import Simple
from django.contrib.auth.models import User, auth



# Create your views here.

def test(request) :
    header_str = 'Test management 123'
    context = {
   'var1' : header_str

    }
    
    return render(request,'test.html', context)


def test1(request) :
    template = loader.get_template('test1.html')
    queryset = Simple.objects.all()
    context = {
    'var2' : queryset
    }

    return HttpResponse(template.render(context, request))

class Homeview(View) :
    template_name = 'test2.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self,request) :
        form = HomeForm(request.POST)
        line_test = Simple.objects.all()
        line = LineAPI.lineNotify(line_test)
        if form.is_valid():
            text = form.cleaned_data['post']
            print(line)

        args = {'form': form, 'text': text }
        return render(request,self.template_name, args)

def test3(request) :
    template = loader.get_template('test3.html')
    queryset = Simple.objects.all()
    context = {
    'var3' : queryset
    }

    return HttpResponse(template.render(context, request))

def test4(request) :
    template = loader.get_template('test4.html')
    queryset = Simple.objects.all()
    context = {
    'var4' : queryset
    }

    return HttpResponse(template.render(context, request))

def register(request) :

    if request.method == 'POST' :
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pw1 = request.POST['pw1']
        pw2 = request.POST['pw2']

        if pw1==pw2 :
            if User.objects.filter(username=uname).exists():
                print('Username taken')
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, username=uname, password=pw1)
                user.save();
                print('user created')

        else: 
            print('password not matching...') 
        return redirect('/my_index')

    else:
        return render(request,'test5.html')

def test6(request) :
    template = loader.get_template('test6.html')
    header_str = 'Test management 123'
    context = {
    'var6' : header_str
    }

    return HttpResponse(template.render(context, request))




 
