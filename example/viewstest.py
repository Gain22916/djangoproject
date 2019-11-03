from django.shortcuts import render, redirect
from django.template import loader
from .models import Simple
from django.http import HttpResponse
from example.forms import HomeForm
from django.views import View
import requests
from admin_management import LineAPI
from example.models import Simple, Intruder, Errormessage
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from example import TestLine



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
                messages.info(request,'Username Taken')
                print('Username taken')
                return redirect('/accounts/register')
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, username=uname, password=pw1)
                user.save();
                print('user created')
                return redirect('/accounts/login')

        elif uname == '' :
            messages.info(request,'Please provide Username')
            print('user blank')
            return redirect('/accounts/register')
        
        elif pw1 == '':
            messages.info(request,'Please provide Password')
            print('password blank')
            return redirect('/accounts/register')

        elif pw2 == '':
            messages.info(request,'Please confirm Password')
            print('password blank')
            return redirect('/accounts/register')

        elif pw1 == '' and pw2 == '':
            messages.info(request,'Please provide Password and confirm Password')
            print('password blank')
            return redirect('/accounts/register')

        else: 
            print('password not matching...')
            messages.info(request,'password not matching...')
            return redirect('/accounts/register') 
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

def login(request) :

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print('login successfully')
            login(request, user)   
            return redirect('/my_index')
        else:
            print('login failed')
            messages.info(request, 'Invalid credentials')
            return redirect('/accounts/login')
    else:
        return render(request,'test7.html')


 
def test8(request) :
    template = loader.get_template('test8.html')
    header_str = 'Intruder History'
    posts = Intruder.objects.all()

    args = {'var8': header_str, 'posts': posts }

    return HttpResponse(template.render(args, request))
    
class Linetest(View) :
    template_name = 'test9.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
        post_intru = Intruder.objects.all()
        for intruder in post_intru:
            #print(intruder.Intru, "--", intruder.IPcam)
            last_Intru = request.POST['Intruder']
            last_IPcam = request.POST['Ipcamera']
            last_Time = request.POST['Time'] 
            last_Image = request.POST['ImageID']
        form = HomeForm(request.POST)
        line_text = TestLine.line_text(last_Intru)
        line_text = TestLine.line_text(last_IPcam)
        line_text = TestLine.line_text(last_Time)
        line_text = TestLine.line_text(last_Image)
        line_pic = TestLine.line_pic("Test", last_Image)
        #add object into database 
        b2 = Intruder(Intru=last_Intru,IPcam=last_IPcam, Time=last_Time, ImageID=last_Image)
        b2.save()


        #Edit object into database

        
        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
            print(line_text)
            print(line_pic)
       
        args = {'form': form}
        return render(request,self.template_name, args)

def test10(request) :
    template = loader.get_template('test10.html')
    header_str = 'IP camera connection testing'

    args = {'var10': header_str}

    return HttpResponse(template.render(args, request))

def test11(request) :
    template = loader.get_template('test11.html')
    header_str = 'ERROR management testing'

    args = {'var11': header_str}

    return HttpResponse(template.render(args, request))


def loginpage(request) :
    template = loader.get_template('loginpage.html')
    header_str = 'Login page testing'

    args = {'var12': header_str}


    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        #Admin : username and Password (Admin ID)
        if username == 'admin' and password =='1234' :
            print('login successfully')
            return redirect('/mainpage/')
        else:
            print('login failed')
            messages.info(request,'Login failed : Please validation')
            return redirect('/loginpage/')

    return HttpResponse(template.render(args, request))


def mainpage(request) :
    template = loader.get_template('mainpage.html')
    header_str = 'Login page testing'
    posts = Intruder.objects.all()
    posts2 = Errormessage.objects.all()

    args = {'var12': header_str, 'posts': posts, 'posts2': posts2}

    return HttpResponse(template.render(args, request))

def test12(request) :
    template = loader.get_template('test12.html')
    header_str = 'Test modal pop up'

    args = {'var12': header_str}

    return HttpResponse(template.render(args, request))

def test13(request) :
    template = loader.get_template('test13.html')
    header_str = 'Test change status'

    args = {'var13': header_str}

    return HttpResponse(template.render(args, request))


