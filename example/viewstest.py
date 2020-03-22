from django.shortcuts import render, redirect
from django.template import loader
from .models import Simple
from django.http import HttpResponse
from example.forms import HomeForm
from django.views import View
import requests
from admin_management import LineAPI
from example.models import Simple, Intruder, Errormessage, IPstatus,overviewStatus,daily_feeds,camera_notification
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from example import TestLine
import time, datetime
from datetime import datetime



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


#login method for login page
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

##############!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!####################
#Line integration: major code in order to recieve Post method from OD system code
class Linetest(View) :
    template_name = 'test9.html' #reference template refer to OD system (Post method path)
    
    # Get method
    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    # Post Method*****
    def post(self, request):
        print(type(request)) 
        post_intru = Intruder.objects.all() 
        last_blanck = "                         "
        last_End = "  ------ End ------  " # last text for line notification content
        # current date and time
        now = datetime.now()
        ticks = now.strftime("%d/%m/%Y, %H:%M:%S")


        #Filter_Feature_Variables

        #Human_filter
        filter_a = overviewStatus.objects.get(id=6)
        filter_b = filter_a.Over_num

        #CAT_filter
        filter_c = overviewStatus.objects.get(id=7)
        filter_d = filter_c.Over_num

        #Snake_filter
        filter_e = overviewStatus.objects.get(id=8)
        filter_f = filter_e.Over_num

        #IPcameraNotification variable for filter function of IP camera
        CAM_N001 = camera_notification.objects.get(id=1)
        CAM_N002 = CAM_N001.CameraNoti_status
        CAM_N003 = camera_notification.objects.get(id=2)
        CAM_N004 = CAM_N003.CameraNoti_status
        CAM_N005 = camera_notification.objects.get(id=3)
        CAM_N006 = CAM_N005.CameraNoti_status
        CAM_N007 = camera_notification.objects.get(id=4)
        CAM_N008 = CAM_N007.CameraNoti_status
        CAM_N009 = camera_notification.objects.get(id=5)
        CAM_N010 = CAM_N009.CameraNoti_status
        CAM_N011 = camera_notification.objects.get(id=6)
        CAM_N012 = CAM_N011.CameraNoti_status
        CAM_N013 = camera_notification.objects.get(id=7)
        CAM_N014 = CAM_N013.CameraNoti_status
        CAM_N015 = camera_notification.objects.get(id=8)
        CAM_N016 = CAM_N015.CameraNoti_status
        CAM_N017 = camera_notification.objects.get(id=9)
        CAM_N018 = CAM_N017.CameraNoti_status
        CAM_N019 = camera_notification.objects.get(id=10)
        CAM_N020 = CAM_N019.CameraNoti_status
        CAM_N021 = camera_notification.objects.get(id=11)
        CAM_N022 = CAM_N021.CameraNoti_status
        CAM_N023 = camera_notification.objects.get(id=12)
        CAM_N024 = CAM_N023.CameraNoti_status
        CAM_N025 = camera_notification.objects.get(id=13)
        CAM_N026 = CAM_N025.CameraNoti_status
        CAM_N027 = camera_notification.objects.get(id=14)
        CAM_N028 = CAM_N027.CameraNoti_status
        CAM_N029 = camera_notification.objects.get(id=15)
        CAM_N030 = CAM_N029.CameraNoti_status
        CAM_N031 = camera_notification.objects.get(id=16)
        CAM_N032 = CAM_N031.CameraNoti_status
        CAM_N033 = camera_notification.objects.get(id=17)
        CAM_N034 = CAM_N033.CameraNoti_status
        CAM_N035 = camera_notification.objects.get(id=18)
        CAM_N036 = CAM_N035.CameraNoti_status 
        CAM_N037 = camera_notification.objects.get(id=19)
        CAM_N038 = CAM_N037.CameraNoti_status 
        CAM_N039 = camera_notification.objects.get(id=20)
        CAM_N040 = CAM_N039.CameraNoti_status 
        CAM_N041 = camera_notification.objects.get(id=21)
        CAM_N042 = CAM_N041.CameraNoti_status 
        CAM_N043 = camera_notification.objects.get(id=22)
        CAM_N044 = CAM_N043.CameraNoti_status 
        CAM_N045 = camera_notification.objects.get(id=23)
        CAM_N046 = CAM_N045.CameraNoti_status 
        CAM_N047 = camera_notification.objects.get(id=24)
        CAM_N048 = CAM_N047.CameraNoti_status 
        CAM_N049 = camera_notification.objects.get(id=25)
        CAM_N050 = CAM_N049.CameraNoti_status
        #IPcameraNotification 2 # protect ERROR code of limitation
        CAM_N051 = camera_notification.objects.get(id=26)
        CAM_N052 = CAM_N051.CameraNoti_status  
        CAM_N053 = camera_notification.objects.get(id=27)
        CAM_N054 = CAM_N053.CameraNoti_status 
        CAM_N055 = camera_notification.objects.get(id=28)
        CAM_N056 = CAM_N055.CameraNoti_status 

        # Picture result path for admin system in the part of intruder history 
        position_path = '/code/admin-webpage/example/static/images/' #adjust for Production away first

        #receive the valiable of POST (OD system)
        for intruder in post_intru:
            last_Intru = request.POST['Intruder'] # receive Intruder name : Human, Cat&Dog , Snake
            last_IPcam = request.POST['Ipcamera'] # receive IP camera name : CAM001 , CAM002 etc.
            last_Time = request.POST['Time'] # receive detected time : 01/01/2020 10.00 AM
            last_Image = request.POST['ImageID'] # receive picture result name for intruder history

        form = HomeForm(request.POST)
        #add object into database based on SQLlite3
        b2 = Intruder(Intru=last_Intru,IPcam=last_IPcam, Time=last_Time, ImageID=last_Image)
        b2.save()
        #add daily feeds into database for overall status page
        d2 = daily_feeds(daily_name='ระบบตรวจจับผู้บุกรุกเป็น: ' + last_Intru, daly_time=ticks )
        d2.save()

        #back up code
        #line_text = TestLine.line_text(last_Intru)
        #line_text = TestLine.line_text(last_IPcam)
        #line_text = TestLine.line_text(last_Time)
        #line_text = TestLine.line_text(last_Image)

       
        # filter function for all IP camera

        if filter_b == '1' and last_Intru == 'Human':

            if CAM_N002 == '1' and last_IPcam =='CAM001' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N004 == '1' and last_IPcam =='CAM002' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N006 == '1' and last_IPcam =='CAM003' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N008 == '1' and last_IPcam =='CAM004' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N010 == '1' and last_IPcam =='CAM005' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N012 == '1' and last_IPcam =='CAM006' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N014 == '1' and last_IPcam =='CAM007' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N016 == '1' and last_IPcam =='CAM008' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N018 == '1' and last_IPcam =='CAM009' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N020 == '1' and last_IPcam =='CAM010' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N022 == '1' and last_IPcam =='CAM011' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N024 == '1' and last_IPcam =='CAM012' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N026 == '1' and last_IPcam =='CAM013' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N028 == '1' and last_IPcam =='CAM014' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N030 == '1' and last_IPcam =='CAM015' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N032 == '1' and last_IPcam =='CAM016' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N034 == '1' and last_IPcam =='CAM017' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N036 == '1' and last_IPcam =='CAM018' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N038 == '1' and last_IPcam =='CAM019' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N040 == '1' and last_IPcam =='CAM020' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N042 == '1' and last_IPcam =='CAM021' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N044 == '1' and last_IPcam =='CAM022' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N046 == '1' and last_IPcam =='CAM023' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N048 == '1' and last_IPcam =='CAM024' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N050 == '1' and last_IPcam =='CAM025' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N052 == '1' and last_IPcam =='CAM026' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N054 == '1' and last_IPcam =='CAM027' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N056 == '1' and last_IPcam =='CAM028' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)



        elif filter_d == '1' and last_Intru == 'Cat&Dog':
        
            if CAM_N002 == '1' and last_IPcam =='CAM001' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N004 == '1' and last_IPcam =='CAM002' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N006 == '1' and last_IPcam =='CAM003' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N008 == '1' and last_IPcam =='CAM004' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N010 == '1' and last_IPcam =='CAM005' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N012 == '1' and last_IPcam =='CAM006' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N014 == '1' and last_IPcam =='CAM007' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N016 == '1' and last_IPcam =='CAM008' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N018 == '1' and last_IPcam =='CAM009' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N020 == '1' and last_IPcam =='CAM010' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N022 == '1' and last_IPcam =='CAM011' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N024 == '1' and last_IPcam =='CAM012' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N026 == '1' and last_IPcam =='CAM013' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N028 == '1' and last_IPcam =='CAM014' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N030 == '1' and last_IPcam =='CAM015' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N032 == '1' and last_IPcam =='CAM016' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N034 == '1' and last_IPcam =='CAM017' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N036 == '1' and last_IPcam =='CAM018' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N038 == '1' and last_IPcam =='CAM019' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N040 == '1' and last_IPcam =='CAM020' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N042 == '1' and last_IPcam =='CAM021' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N044 == '1' and last_IPcam =='CAM022' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N046 == '1' and last_IPcam =='CAM023' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N048 == '1' and last_IPcam =='CAM024' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N050 == '1' and last_IPcam =='CAM025' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N052 == '1' and last_IPcam =='CAM026' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N054 == '1' and last_IPcam =='CAM027' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N056 == '1' and last_IPcam =='CAM028' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

        elif filter_f == '1' and last_Intru == 'Snake':
        
            if CAM_N002 == '1' and last_IPcam =='CAM001' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N004 == '1' and last_IPcam =='CAM002' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N006 == '1' and last_IPcam =='CAM003' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N008 == '1' and last_IPcam =='CAM004' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N010 == '1' and last_IPcam =='CAM005' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N012 == '1' and last_IPcam =='CAM006' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N014 == '1' and last_IPcam =='CAM007' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N016 == '1' and last_IPcam =='CAM008' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N018 == '1' and last_IPcam =='CAM009' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N020 == '1' and last_IPcam =='CAM010' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N022 == '1' and last_IPcam =='CAM011' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N024 == '1' and last_IPcam =='CAM012' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N026 == '1' and last_IPcam =='CAM013' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N028 == '1' and last_IPcam =='CAM014' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)
            
            elif CAM_N030 == '1' and last_IPcam =='CAM015' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N032 == '1' and last_IPcam =='CAM016' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N034 == '1' and last_IPcam =='CAM017' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N036 == '1' and last_IPcam =='CAM018' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N038 == '1' and last_IPcam =='CAM019' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N040 == '1' and last_IPcam =='CAM020' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N042 == '1' and last_IPcam =='CAM021' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N044 == '1' and last_IPcam =='CAM022' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N046 == '1' and last_IPcam =='CAM023' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N048 == '1' and last_IPcam =='CAM024' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N050 == '1' and last_IPcam =='CAM025' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N052 == '1' and last_IPcam =='CAM026' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N054 == '1' and last_IPcam =='CAM027' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)

            elif CAM_N056 == '1' and last_IPcam =='CAM028' :
                line_pic = TestLine.line_pic(last_IPcam ,position_path + last_Image)
                line_text = TestLine.line_text(last_End)


        #########back up code########
        #line_text = TestLine.line_text(last_Intru)
        #line_text = TestLine.line_text(last_IPcam)
        #line_text = TestLine.line_text(last_Time)
        #line_text = TestLine.line_text(last_Image)
        #line_pic = TestLine.line_pic("Test", last_Image)

        #Edit object from database

        #b4 = overviewStatus(id=3, IPnum='CAM003',IPcam='Not123', Time='Not123', ImageID='Not123')
        #b4.save()

        #Delete object from database
        #Intruder.objects.filter(id=1).delete()
        ##########################################

        if form.is_valid():
            text = form.cleaned_data['post']   
            print(line_pic)
            print(line_text)
       
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


# username & passwords for login page !!!!!!!!!!!
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
            messages.info(request,'การเข้าระบบผิดพลาด : โปรดตรวจสอบ')
            return redirect('/loginpage/')

    return HttpResponse(template.render(args, request))


# main page for overall status and all tabs of admin system !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Main_page(View) :
    template_name = 'mainpage.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        header_str = 'Login page '
        posts = Intruder.objects.all().order_by('id')[:4000] # data limitation for intruder data showing
        posts2 = Errormessage.objects.all().order_by('id')[:40] # data limitation for ERROR data showing
        #postsD = daily_feeds.objects.all()
        postsD = daily_feeds.objects.all().order_by('-id')[:20][::-1] # data limitation for daily feed data showing
        #all variable for all status of admin system
        posts4  = IPstatus.objects.get(id=1)
        posts3 = posts4.IPconnect
        posts5 = 'Active'
        posts6 = 'Inactive'
        posts7 = overviewStatus.objects.get(id=1)
        posts8 = posts7.Over_num
        posts9 = 'Morning'
        posts10 = 'Night & Raining'
        posts11 = overviewStatus.objects.get(id=2)
        posts12 = posts11.Over_num
        posts13 = overviewStatus.objects.get(id=3)
        posts14 = posts13.Over_num
        posts15 = overviewStatus.objects.get(id=4)
        posts16 = posts15.Over_num
        posts17 = overviewStatus.objects.get(id=5)
        posts18 = posts17.Over_num
        posts19 = IPstatus.objects.get(id=2)
        posts20 = posts19.IPconnect
        posts21 = IPstatus.objects.get(id=3)
        posts22 = posts21.IPconnect
        posts23 = IPstatus.objects.get(id=4)
        posts24 = posts23.IPconnect
        posts25 = IPstatus.objects.get(id=5)
        posts26 = posts25.IPconnect
        posts27 = IPstatus.objects.get(id=6)
        posts28 = posts27.IPconnect
        posts29 = IPstatus.objects.get(id=7)
        posts30 = posts29.IPconnect
        posts31 = IPstatus.objects.get(id=8)
        posts32 = posts31.IPconnect
        posts33 = IPstatus.objects.get(id=9)
        posts34 = posts33.IPconnect
        posts35 = IPstatus.objects.get(id=10)
        posts36 = posts35.IPconnect
        posts37 = IPstatus.objects.get(id=11)
        posts38 = posts37.IPconnect
        posts39 = IPstatus.objects.get(id=12)
        posts40 = posts39.IPconnect
        posts41 = IPstatus.objects.get(id=13)
        posts42 = posts41.IPconnect
        posts43 = IPstatus.objects.get(id=14)
        posts44 = posts43.IPconnect
        posts45 = IPstatus.objects.get(id=15)
        posts46 = posts45.IPconnect
        posts47 = IPstatus.objects.get(id=16)
        posts48 = posts47.IPconnect
        posts49 = IPstatus.objects.get(id=17)
        posts50 = posts49.IPconnect
        posts51 = IPstatus.objects.get(id=18)
        posts52 = posts51.IPconnect
        posts53 = IPstatus.objects.get(id=19)
        posts54 = posts53.IPconnect
        posts55 = IPstatus.objects.get(id=20)
        posts56 = posts55.IPconnect
        posts57 = IPstatus.objects.get(id=21)
        posts58 = posts57.IPconnect
        posts59 = IPstatus.objects.get(id=22)
        posts60 = posts59.IPconnect
        posts61 = IPstatus.objects.get(id=23)
        posts62 = posts61.IPconnect
        posts63 = IPstatus.objects.get(id=24)
        posts64 = posts63.IPconnect
        posts65 = IPstatus.objects.get(id=25)
        posts66 = posts65.IPconnect
        posts67 = IPstatus.objects.get(id=26)
        posts68 = posts67.IPconnect
        posts69 = IPstatus.objects.get(id=27)
        posts70 = posts69.IPconnect
        posts71 = IPstatus.objects.get(id=28)
        posts72 = posts71.IPconnect
        posts73 = overviewStatus.objects.get(id=6)
        posts74 = posts73.Over_num
        posts75 = overviewStatus.objects.get(id=7)
        posts76 = posts75.Over_num
        posts77 = overviewStatus.objects.get(id=8)
        posts78 = posts77.Over_num
        #Camera notification status 
        posts79 = camera_notification.objects.get(id=1)
        posts80 = posts79.CameraNoti_status
        posts81 = camera_notification.objects.get(id=2)
        posts82 = posts81.CameraNoti_status
        posts83 = camera_notification.objects.get(id=3)
        posts84 = posts83.CameraNoti_status
        posts85 = camera_notification.objects.get(id=4)
        posts86 = posts85.CameraNoti_status
        posts87 = camera_notification.objects.get(id=5)
        posts88 = posts87.CameraNoti_status
        posts89 = camera_notification.objects.get(id=6)
        posts90 = posts89.CameraNoti_status
        posts91 = camera_notification.objects.get(id=7)
        posts92 = posts91.CameraNoti_status
        posts93 = camera_notification.objects.get(id=8)
        posts94 = posts93.CameraNoti_status
        posts95 = camera_notification.objects.get(id=9)
        posts96 = posts95.CameraNoti_status
        posts97 = camera_notification.objects.get(id=10)
        posts98 = posts97.CameraNoti_status
        posts99 = camera_notification.objects.get(id=11)
        posts100 = posts99.CameraNoti_status
        posts101 = camera_notification.objects.get(id=12)
        posts102 = posts101.CameraNoti_status
        posts103 = camera_notification.objects.get(id=13)
        posts104 = posts103.CameraNoti_status
        posts105 = camera_notification.objects.get(id=14)
        posts106 = posts105.CameraNoti_status
        posts107 = camera_notification.objects.get(id=15)
        posts108 = posts107.CameraNoti_status
        posts109 = camera_notification.objects.get(id=16)
        posts110 = posts109.CameraNoti_status
        posts111 = camera_notification.objects.get(id=17)
        posts112 = posts111.CameraNoti_status
        posts113 = camera_notification.objects.get(id=18)
        posts114 = posts113.CameraNoti_status
        posts115 = camera_notification.objects.get(id=19)
        posts116 = posts115.CameraNoti_status
        posts117 = camera_notification.objects.get(id=20)
        posts118 = posts117.CameraNoti_status
        posts119 = camera_notification.objects.get(id=21)
        posts120 = posts119.CameraNoti_status
        posts121 = camera_notification.objects.get(id=22)
        posts122 = posts121.CameraNoti_status
        posts123 = camera_notification.objects.get(id=23)
        posts124 = posts123.CameraNoti_status
        posts125 = camera_notification.objects.get(id=24)
        posts126 = posts125.CameraNoti_status
        posts127 = camera_notification.objects.get(id=25)
        posts128 = posts127.CameraNoti_status
        posts129 = camera_notification.objects.get(id=26)
        posts130 = posts129.CameraNoti_status
        posts131 = camera_notification.objects.get(id=27)
        posts132 = posts131.CameraNoti_status
        posts133 = camera_notification.objects.get(id=28)
        posts134 = posts133.CameraNoti_status



        # current date and time
        now = datetime.now()
        ticks = now.strftime("%d/%m/%Y, %H:%M:%S")

    
        if posts3 == '1' and posts20 == '1' and posts22 == '1' and posts24 == '1' and posts26 == '1' and posts28 == '1' and posts30 == '1' and posts32 == '1' and posts34 == '1' and posts36 == '1' and posts38 == '1' and posts40 == '1' and posts42 == '1' and posts44 == '1' and posts46 == '1' and posts48 == '1' and posts50 == '1' and posts52 == '1' and posts54 == '1' and posts56 == '1' and posts58 == '1' and posts60 == '1' and posts62 == '1' and posts64 == '1' and posts66 == '1' and posts68 == '1' and posts70 == '1' and posts72 == '1' :
            #Edit object into database for OD system status
            b10 = overviewStatus(id=2, Over_name='IPcameraConnection', Over_num='1' )
            b10.save()
            b11 = overviewStatus(id=3, Over_name='ODsystem', Over_num='1' )
            b11.save()

            
        else: 
            #Edit object into database for OD system status
            b12 = overviewStatus(id=2, Over_name='IPcameraConnection', Over_num='0' )
            b12.save()
            b13 = overviewStatus(id=3, Over_name='ODsystem', Over_num='0' )
            b13.save()


        args = {'var12': header_str, 'posts': posts, 'posts2': posts2, 'posts3' : posts3, 'posts5' : posts5, 'posts6' : posts6, 'posts8' : posts8, 'posts9' : posts9, 'posts10' : posts10, 'posts12' : posts12, 'posts14' : posts14, 'posts16' : posts16, 'posts18' : posts18, 'posts20' : posts20, 'posts22' : posts22, 'posts24' : posts24, 'posts26' : posts26, 'posts28' : posts28, 'posts30' : posts30, 'posts32' : posts32, 'posts34' : posts34, 'posts36' : posts36, 'posts38' : posts38, 'posts40' : posts40, 'posts42' : posts42, 'posts44' : posts44, 'posts46' : posts46, 'posts48' : posts48, 'posts50' : posts50, 'posts52' : posts52, 'posts54' : posts54, 'posts56' : posts56, 'posts58' : posts58,'posts60' : posts60,'posts62' : posts62,'posts64' : posts64, 'posts66' : posts66, 'posts68' : posts68, 'posts70' : posts70, 'posts72' : posts72, 'posts74' : posts74, 'posts76' : posts76, 'posts78' : posts78, 'postsD' : postsD, 'posts80' : posts80, 'posts82' : posts82, 'posts84' : posts84, 'posts86' : posts86, 'posts88' : posts88, 'posts90' : posts90, 'posts92' : posts92, 'posts94' : posts94, 'posts96' : posts96, 'posts98' : posts98, 'posts100' : posts100, 'posts102' : posts102, 'posts104' : posts104, 'posts106' : posts106, 'posts108' : posts108, 'posts110' : posts110, 'posts112' : posts112, 'posts114' : posts114, 'posts116' : posts116, 'posts118' : posts118, 'posts120' : posts120, 'posts122' : posts122, 'posts124' : posts124, 'posts126' : posts126, 'posts128' : posts128, 'posts130' : posts130, 'posts132' : posts132, 'posts134' : posts134  }
        return render(request,self.template_name, args)

    #Post method in order to change status of system (General setting; on off status and on off detection )
    def post(self, request):
        print(type(request))
        template = loader.get_template('mainpage.html')
        header_str = 'Post Method'
        form = HomeForm()
        header_str = 'Login page testing'
        posts = Intruder.objects.all().order_by('id')[:2000]
        posts2 = Errormessage.objects.all().order_by('id')[:20]
        #postsD = daily_feeds.objects.all()
        postsD = daily_feeds.objects.all().order_by('-id')[:20][::-1]
        posts4  = IPstatus.objects.get(id=1)
        posts3 = posts4.IPconnect
        posts5 = 'Active'
        posts6 = 'Inactive'
        posts7 = overviewStatus.objects.get(id=1)
        posts8 = posts7.Over_num
        posts9 = 'Morning'
        posts10 = 'Night & Raining'
        posts11 = overviewStatus.objects.get(id=2)
        posts12 = posts11.Over_num
        posts13 = overviewStatus.objects.get(id=3)
        posts14 = posts13.Over_num
        posts15 = overviewStatus.objects.get(id=4)
        posts16 = posts15.Over_num
        posts17 = overviewStatus.objects.get(id=5)
        posts18 = posts17.Over_num
        posts19 = IPstatus.objects.get(id=2)
        posts20 = posts19.IPconnect
        posts21 = IPstatus.objects.get(id=3)
        posts22 = posts21.IPconnect
        posts23 = IPstatus.objects.get(id=4)
        posts24 = posts23.IPconnect
        posts25 = IPstatus.objects.get(id=5)
        posts26 = posts25.IPconnect
        posts27 = IPstatus.objects.get(id=6)
        posts28 = posts27.IPconnect
        posts29 = IPstatus.objects.get(id=7)
        posts30 = posts29.IPconnect
        posts31 = IPstatus.objects.get(id=8)
        posts32 = posts31.IPconnect
        posts33 = IPstatus.objects.get(id=9)
        posts34 = posts33.IPconnect
        posts35 = IPstatus.objects.get(id=10)
        posts36 = posts35.IPconnect
        posts37 = IPstatus.objects.get(id=11)
        posts38 = posts37.IPconnect
        posts39 = IPstatus.objects.get(id=12)
        posts40 = posts39.IPconnect
        posts41 = IPstatus.objects.get(id=13)
        posts42 = posts41.IPconnect
        posts43 = IPstatus.objects.get(id=14)
        posts44 = posts43.IPconnect
        posts45 = IPstatus.objects.get(id=15)
        posts46 = posts45.IPconnect
        posts47 = IPstatus.objects.get(id=16)
        posts48 = posts47.IPconnect
        posts49 = IPstatus.objects.get(id=17)
        posts50 = posts49.IPconnect
        posts51 = IPstatus.objects.get(id=18)
        posts52 = posts51.IPconnect
        posts53 = IPstatus.objects.get(id=19)
        posts54 = posts53.IPconnect
        posts55 = IPstatus.objects.get(id=20)
        posts56 = posts55.IPconnect
        posts57 = IPstatus.objects.get(id=21)
        posts58 = posts57.IPconnect
        posts59 = IPstatus.objects.get(id=22)
        posts60 = posts59.IPconnect
        posts61 = IPstatus.objects.get(id=23)
        posts62 = posts61.IPconnect
        posts63 = IPstatus.objects.get(id=24)
        posts64 = posts63.IPconnect
        posts65 = IPstatus.objects.get(id=25)
        posts66 = posts65.IPconnect
        posts67 = IPstatus.objects.get(id=26)
        posts68 = posts67.IPconnect
        posts69 = IPstatus.objects.get(id=27)
        posts70 = posts69.IPconnect
        posts71 = IPstatus.objects.get(id=28)
        posts72 = posts71.IPconnect
        posts73 = overviewStatus.objects.get(id=6)
        posts74 = posts73.Over_num
        posts75 = overviewStatus.objects.get(id=7)
        posts76 = posts75.Over_num
        posts77 = overviewStatus.objects.get(id=8)
        posts78 = posts77.Over_num
        #Camera notification status
        posts79 = camera_notification.objects.get(id=1)
        posts80 = posts79.CameraNoti_status
        posts81 = camera_notification.objects.get(id=2)
        posts82 = posts81.CameraNoti_status
        posts83 = camera_notification.objects.get(id=3)
        posts84 = posts83.CameraNoti_status
        posts85 = camera_notification.objects.get(id=4)
        posts86 = posts85.CameraNoti_status
        posts87 = camera_notification.objects.get(id=5)
        posts88 = posts87.CameraNoti_status
        posts89 = camera_notification.objects.get(id=6)
        posts90 = posts89.CameraNoti_status
        posts91 = camera_notification.objects.get(id=7)
        posts92 = posts91.CameraNoti_status
        posts93 = camera_notification.objects.get(id=8)
        posts94 = posts93.CameraNoti_status
        posts95 = camera_notification.objects.get(id=9)
        posts96 = posts95.CameraNoti_status
        posts97 = camera_notification.objects.get(id=10)
        posts98 = posts97.CameraNoti_status
        posts99 = camera_notification.objects.get(id=11)
        posts100 = posts99.CameraNoti_status
        posts101 = camera_notification.objects.get(id=12)
        posts102 = posts101.CameraNoti_status
        posts103 = camera_notification.objects.get(id=13)
        posts104 = posts103.CameraNoti_status
        posts105 = camera_notification.objects.get(id=14)
        posts106 = posts105.CameraNoti_status
        posts107 = camera_notification.objects.get(id=15)
        posts108 = posts107.CameraNoti_status
        posts109 = camera_notification.objects.get(id=16)
        posts110 = posts109.CameraNoti_status
        posts111 = camera_notification.objects.get(id=17)
        posts112 = posts111.CameraNoti_status
        posts113 = camera_notification.objects.get(id=18)
        posts114 = posts113.CameraNoti_status
        posts115 = camera_notification.objects.get(id=19)
        posts116 = posts115.CameraNoti_status
        posts117 = camera_notification.objects.get(id=20)
        posts118 = posts117.CameraNoti_status
        posts119 = camera_notification.objects.get(id=21)
        posts120 = posts119.CameraNoti_status
        posts121 = camera_notification.objects.get(id=22)
        posts122 = posts121.CameraNoti_status
        posts123 = camera_notification.objects.get(id=23)
        posts124 = posts123.CameraNoti_status
        posts125 = camera_notification.objects.get(id=24)
        posts126 = posts125.CameraNoti_status
        posts127 = camera_notification.objects.get(id=25)
        posts128 = posts127.CameraNoti_status
        posts129 = camera_notification.objects.get(id=26)
        posts130 = posts129.CameraNoti_status
        posts131 = camera_notification.objects.get(id=27)
        posts132 = posts131.CameraNoti_status
        posts133 = camera_notification.objects.get(id=28)
        posts134 = posts133.CameraNoti_status

        # current date and time
        now = datetime.now()
        ticks = now.strftime("%d/%m/%Y, %H:%M:%S")
    
        if posts3 == '1' and posts20 == '1' and posts22 == '1' and posts24 == '1' and posts26 == '1' and posts28 == '1' and posts30 == '1' and posts32 == '1' and posts34 == '1' and posts36 == '1' and posts38 == '1' and posts40 == '1' and posts42 == '1' and posts44 == '1' and posts46 == '1' and posts48 == '1' and posts50 == '1' and posts52 == '1' and posts54 == '1' and posts56 == '1' and posts58 == '1' and posts60 == '1' and posts62 == '1' and posts64 == '1' and posts66 == '1' and posts68 == '1' and posts70 == '1' and posts72 == '1' :
            #Edit object into database
            b10 = overviewStatus(id=2, Over_name='IPcameraConnection', Over_num='1' )
            b10.save()
            b11 = overviewStatus(id=3, Over_name='ODsystem', Over_num='1' )
            b11.save()

            #Add object into database
            d6 = daily_feeds(daily_name='ระบบตรวจจับผู้บุกรุก: ทำงาน ', daly_time=ticks )
            d6.save()

        else: 
            #Edit object into database
            b12 = overviewStatus(id=2, Over_name='IPcameraConnection', Over_num='0' )
            b12.save()
            b13 = overviewStatus(id=3, Over_name='ODsystem', Over_num='0' )
            b13.save()

            #Add object into database
            d8 = daily_feeds(daily_name='ระบบตรวจจับผู้บุกรุก: ไม่ทำงาน ', daly_time=ticks )
            d8.save()


        #POST

        form = HomeForm(request.POST)
        var001 = str(request.POST["Value1"])
       
        print(var001)
        # on off function of Object detection
        if var001 == "G" :
            f01 = overviewStatus(id=6, Over_name='HumanFilter', Over_num='1' )
            f01.save()

            #Add object into database
            d10 = daily_feeds(daily_name='การตรวจจับมนุษย์: ทำงานปกติ ', daly_time=ticks )
            d10.save()
            
        elif var001 == "H" :
            f02 = overviewStatus(id=6, Over_name='HumanFilter', Over_num='0' )
            f02.save()

            #Add object into database
            d12 = daily_feeds(daily_name='การตรวจจับมนุษย์: ไม่ทำงาน ', daly_time=ticks )
            d12.save()

        elif var001 == "I" :
            f03 = overviewStatus(id=7, Over_name='CatFilter', Over_num='1' )
            f03.save()

            #Add object into database
            d14 = daily_feeds(daily_name='การตรวจจับแมวและสุนัข: ทำงานปกติ ', daly_time=ticks )
            d14.save()
        
        elif var001 == "J" :
            f04 = overviewStatus(id=7, Over_name='CatFilter', Over_num='0' )
            f04.save()

            #Add object into database
            d16 = daily_feeds(daily_name='การตรวจจับแมวและสุนัข: ไม่ทำงาน ', daly_time=ticks )
            d16.save()

        elif var001 == "K" :
            f05 = overviewStatus(id=8, Over_name='SnakeFilter', Over_num='1' )
            f05.save()

            #Add object into database
            d18 = daily_feeds(daily_name='การตรวจจับงู: ทำงานปกติ ', daly_time=ticks )
            d18.save()

        elif var001 == "L" :
            f06 = overviewStatus(id=8, Over_name='SnakeFilter', Over_num='0' )
            f06.save()

            #Add object into database
            d18 = daily_feeds(daily_name='การตรวจจับงู: ไม่ทำงาน ', daly_time=ticks )
            d18.save()


        #ON OFF Camera notification

        elif var001 == "CO01" :
            cm01 = camera_notification(id=1, CameraNoti_name='CAM001+Notification', CameraNoti_status='1' )
            cm01.save()

            #Add object into database
            d19 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่หนึ่ง', daly_time=ticks )
            d19.save()
        
        
        elif var001 == "CF01" :
            cm02 = camera_notification(id=1, CameraNoti_name='CAM001+Notification', CameraNoti_status='0' )
            cm02.save()

            #Add object into database
            d20 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่หนึ่ง', daly_time=ticks )
            d20.save()

        elif var001 == "CO02" :
            cm03 = camera_notification(id=2, CameraNoti_name='CAM002+Notification', CameraNoti_status='1' )
            cm03.save()

            #Add object into database
            d21 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สอง', daly_time=ticks )
            d21.save()
        
        
        elif var001 == "CF02" :
            cm04 = camera_notification(id=2, CameraNoti_name='CAM002+Notification', CameraNoti_status='0' )
            cm04.save()

            #Add object into database
            d22 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สอง', daly_time=ticks )
            d22.save()

        elif var001 == "CO03" :
            cm05 = camera_notification(id=3, CameraNoti_name='CAM003+Notification', CameraNoti_status='1' )
            cm05.save()

            #Add object into database
            d23 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สาม', daly_time=ticks )
            d23.save()
        
        
        elif var001 == "CF03" :
            cm06 = camera_notification(id=3, CameraNoti_name='CAM003+Notification', CameraNoti_status='0' )
            cm06.save()

            #Add object into database
            d24 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สาม', daly_time=ticks )
            d24.save()

        
        elif var001 == "CO04" :
            cm07 = camera_notification(id=4, CameraNoti_name='CAM004+Notification', CameraNoti_status='1' )
            cm07.save()

            #Add object into database
            d25 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สี่', daly_time=ticks )
            d25.save()
        
        
        elif var001 == "CF04" :
            cm08 = camera_notification(id=4, CameraNoti_name='CAM004+Notification', CameraNoti_status='0' )
            cm08.save()

            #Add object into database
            d26 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สี่', daly_time=ticks )
            d26.save()    

    
        elif var001 == "CO05" :
            cm09 = camera_notification(id=5, CameraNoti_name='CAM005+Notification', CameraNoti_status='1' )
            cm09.save()

            #Add object into database
            d27 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่ห้า', daly_time=ticks )
            d27.save()
        
        
        elif var001 == "CF05" :
            cm10 = camera_notification(id=5, CameraNoti_name='CAM005+Notification', CameraNoti_status='0' )
            cm10.save()

            #Add object into database
            d28 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่ห้า', daly_time=ticks )
            d28.save()     

        elif var001 == "CO06" :
            cm11 = camera_notification(id=6, CameraNoti_name='CAM006+Notification', CameraNoti_status='1' )
            cm11.save()

            #Add object into database
            d29 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่หก', daly_time=ticks )
            d29.save()
        
        
        elif var001 == "CF06" :
            cm12 = camera_notification(id=6, CameraNoti_name='CAM006+Notification', CameraNoti_status='0' )
            cm12.save()

            #Add object into database
            d30 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่หก', daly_time=ticks )
            d30.save()            
    
        elif var001 == "CO07" :
            cm13 = camera_notification(id=7, CameraNoti_name='CAM007+Notification', CameraNoti_status='1' )
            cm13.save()

            #Add object into database
            d31 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่เจ็ด', daly_time=ticks )
            d31.save()
    
        
        elif var001 == "CF07" :
            cm14 = camera_notification(id=7, CameraNoti_name='CAM007+Notification', CameraNoti_status='0' )
            cm14.save()

            #Add object into database
            d32 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่เจ็ด', daly_time=ticks )
            d32.save() 

        elif var001 == "CO08" :
            cm15 = camera_notification(id=8, CameraNoti_name='CAM008+Notification', CameraNoti_status='1' )
            cm15.save()

            #Add object into database
            d33 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่แปด', daly_time=ticks )
            d33.save()
        
        
        elif var001 == "CF08" :
            cm16 = camera_notification(id=8, CameraNoti_name='CAM008+Notification', CameraNoti_status='0' )
            cm16.save()

            #Add object into database
            d34 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่แปด', daly_time=ticks )
            d34.save() 
            
        elif var001 == "CO09" :
            cm17 = camera_notification(id=9, CameraNoti_name='CAM009+Notification', CameraNoti_status='1' )
            cm17.save()

            #Add object into database
            d35 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่ก้าว', daly_time=ticks )
            d35.save()
        
        
        elif var001 == "CF09" :
            cm18 = camera_notification(id=9, CameraNoti_name='CAM009+Notification', CameraNoti_status='0' )
            cm18.save()

            #Add object into database
            d36 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่ก้าว', daly_time=ticks )
            d36.save() 

              
        elif var001 == "CO10" :
            cm17 = camera_notification(id=10, CameraNoti_name='CAM010+Notification', CameraNoti_status='1' )
            cm17.save()

            #Add object into database
            d35 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สิบ', daly_time=ticks )
            d35.save()
        
        
        elif var001 == "CF10" :
            cm18 = camera_notification(id=10, CameraNoti_name='CAM010+Notification', CameraNoti_status='0' )
            cm18.save()

            #Add object into database
            d36 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สิบ', daly_time=ticks )
            d36.save() 


        elif var001 == "CO11" :
            cm19 = camera_notification(id=11, CameraNoti_name='CAM011+Notification', CameraNoti_status='1' )
            cm19.save()

            #Add object into database
            d37 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สิบเอ็ด', daly_time=ticks )
            d37.save()
        
        
        elif var001 == "CF11" :
            cm20 = camera_notification(id=11, CameraNoti_name='CAM011+Notification', CameraNoti_status='0' )
            cm20.save()

            #Add object into database
            d38 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สิบเอ็ด', daly_time=ticks )
            d38.save() 

        elif var001 == "CO12" :
            cm21 = camera_notification(id=12, CameraNoti_name='CAM012+Notification', CameraNoti_status='1' )
            cm21.save()

            #Add object into database
            d39 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สิบสอง', daly_time=ticks )
            d39.save()
        
        
        elif var001 == "CF12" :
            cm22 = camera_notification(id=12, CameraNoti_name='CAM012+Notification', CameraNoti_status='0' )
            cm22.save()

            #Add object into database
            d40 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สิบสอง', daly_time=ticks )
            d40.save()     

        
        elif var001 == "CO13" :
            cm23 = camera_notification(id=13, CameraNoti_name='CAM013+Notification', CameraNoti_status='1' )
            cm23.save()

            #Add object into database
            d41 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สิบสาม', daly_time=ticks )
            d41.save()
        
        
        elif var001 == "CF13" :
            cm24 = camera_notification(id=13, CameraNoti_name='CAM013+Notification', CameraNoti_status='0' )
            cm24.save()

            #Add object into database
            d42 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สิบสาม', daly_time=ticks )
            d42.save()     

        
        elif var001 == "CO14" :
            cm25 = camera_notification(id=14, CameraNoti_name='CAM014+Notification', CameraNoti_status='1' )
            cm25.save()

            #Add object into database
            d43 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สิบสี่', daly_time=ticks )
            d43.save()
        
        
        elif var001 == "CF14" :
            cm26 = camera_notification(id=14, CameraNoti_name='CAM014+Notification', CameraNoti_status='0' )
            cm26.save()

            #Add object into database
            d44 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สิบสี่', daly_time=ticks )
            d44.save()     

     
        elif var001 == "CO15" :
            cm27 = camera_notification(id=15, CameraNoti_name='CAM015+Notification', CameraNoti_status='1' )
            cm27.save()

            #Add object into database
            d45 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สิบห้า', daly_time=ticks )
            d45.save()
        
        
        elif var001 == "CF15" :
            cm28 = camera_notification(id=15, CameraNoti_name='CAM015+Notification', CameraNoti_status='0' )
            cm28.save()

            #Add object into database
            d46 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สิบห้า', daly_time=ticks )
            d46.save()   

    
        elif var001 == "CO16" :
            cm29 = camera_notification(id=16, CameraNoti_name='CAM016+Notification', CameraNoti_status='1' )
            cm29.save()

            #Add object into database
            d47 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สิบหก', daly_time=ticks )
            d47.save()
        
        
        elif var001 == "CF16" :
            cm30 = camera_notification(id=16, CameraNoti_name='CAM016+Notification', CameraNoti_status='0' )
            cm30.save()

            #Add object into database
            d48 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สิบหก', daly_time=ticks )
            d48.save()  


        elif var001 == "CO17" :
            cm31 = camera_notification(id=17, CameraNoti_name='CAM017+Notification', CameraNoti_status='1' )
            cm31.save()

            #Add object into database
            d49 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สิบเจ็ด', daly_time=ticks )
            d49.save()
        
        
        elif var001 == "CF17" :
            cm32 = camera_notification(id=17, CameraNoti_name='CAM017+Notification', CameraNoti_status='0' )
            cm32.save()

            #Add object into database
            d50 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สิบเจ็ด', daly_time=ticks )
            d50.save()  


        elif var001 == "CO18" :
            cm33 = camera_notification(id=18, CameraNoti_name='CAM018+Notification', CameraNoti_status='1' )
            cm33.save()

            #Add object into database
            d51 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สิบแปด', daly_time=ticks )
            d51.save()
        
        
        elif var001 == "CF18" :
            cm34 = camera_notification(id=18, CameraNoti_name='CAM018+Notification', CameraNoti_status='0' )
            cm34.save()

            #Add object into database
            d52 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สิบแปด', daly_time=ticks )
            d52.save() 


        elif var001 == "CO19" :
            cm35 = camera_notification(id=19, CameraNoti_name='CAM019+Notification', CameraNoti_status='1' )
            cm35.save()

            #Add object into database
            d53 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่สิบเก้า', daly_time=ticks )
            d53.save()
        
        
        elif var001 == "CF19" :
            cm36 = camera_notification(id=19, CameraNoti_name='CAM019+Notification', CameraNoti_status='0' )
            cm36.save()

            #Add object into database
            d54 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่สิบเก้า', daly_time=ticks )
            d54.save() 


        elif var001 == "CO20" :
            cm37 = camera_notification(id=20, CameraNoti_name='CAM020+Notification', CameraNoti_status='1' )
            cm37.save()

            #Add object into database
            d55 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบ', daly_time=ticks )
            d55.save()
        
        
        elif var001 == "CF20" :
            cm38 = camera_notification(id=20, CameraNoti_name='CAM020+Notification', CameraNoti_status='0' )
            cm38.save()

            #Add object into database
            d56 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบ', daly_time=ticks )
            d56.save() 


        elif var001 == "CO21" :
            cm39 = camera_notification(id=21, CameraNoti_name='CAM021+Notification', CameraNoti_status='1' )
            cm39.save()

            #Add object into database
            d57 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบเอ็ด', daly_time=ticks )
            d57.save()
        
        
        elif var001 == "CF21" :
            cm40 = camera_notification(id=21, CameraNoti_name='CAM021+Notification', CameraNoti_status='0' )
            cm40.save()

            #Add object into database
            d58 = daily_feeds(daily_name='ปิดการแจ้งเต��อนของกล้องตัวที่ยี่สิบเอ็ด', daly_time=ticks )
            d58.save()


        elif var001 == "CO22" :
            cm42 = camera_notification(id=22, CameraNoti_name='CAM022+Notification', CameraNoti_status='1' )
            cm42.save()

            #Add object into database
            d59 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบสอง', daly_time=ticks )
            d59.save()
        
        
        elif var001 == "CF22" :
            cm43 = camera_notification(id=22, CameraNoti_name='CAM022+Notification', CameraNoti_status='0' )
            cm43.save()

            #Add object into database
            d60 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบสอง', daly_time=ticks )
            d60.save()

        elif var001 == "CO23" :
            cm44 = camera_notification(id=23, CameraNoti_name='CAM023+Notification', CameraNoti_status='1' )
            cm44.save()

            #Add object into database
            d61 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบสาม', daly_time=ticks )
            d61.save()
        
        
        elif var001 == "CF23" :
            cm45 = camera_notification(id=23, CameraNoti_name='CAM023+Notification', CameraNoti_status='0' )
            cm45.save()

            #Add object into database
            d62 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบสาม', daly_time=ticks )
            d62.save()
     

        elif var001 == "CO24" :
            cm46 = camera_notification(id=24, CameraNoti_name='CAM024+Notification', CameraNoti_status='1' )
            cm46.save()

            #Add object into database
            d63 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบสี่', daly_time=ticks )
            d63.save()
        
        
        elif var001 == "CF24" :
            cm47 = camera_notification(id=24, CameraNoti_name='CAM024+Notification', CameraNoti_status='0' )
            cm47.save()

            #Add object into database
            d64 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบสี่', daly_time=ticks )
            d64.save()
     

        elif var001 == "CO25" :
            cm48 = camera_notification(id=25, CameraNoti_name='CAM025+Notification', CameraNoti_status='1' )
            cm48.save()

            #Add object into database
            d65 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบห้า', daly_time=ticks )
            d65.save()
        
        
        elif var001 == "CF25" :
            cm49 = camera_notification(id=25, CameraNoti_name='CAM025+Notification', CameraNoti_status='0' )
            cm49.save()

            #Add object into database
            d66 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบห้า', daly_time=ticks )
            d66.save()


        elif var001 == "CO26" :
            cm50 = camera_notification(id=26, CameraNoti_name='CAM026+Notification', CameraNoti_status='1' )
            cm50.save()

            #Add object into database
            d67 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบหก', daly_time=ticks )
            d67.save()
        
        
        elif var001 == "CF26" :
            cm51 = camera_notification(id=26, CameraNoti_name='CAM026+Notification', CameraNoti_status='0' )
            cm51.save()

            #Add object into database
            d68 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบหก', daly_time=ticks )
            d68.save()


        elif var001 == "CO27" :
            cm52 = camera_notification(id=27, CameraNoti_name='CAM027+Notification', CameraNoti_status='1' )
            cm52.save()

            #Add object into database
            d69 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบเจ็ด', daly_time=ticks )
            d69.save()
        
        
        elif var001 == "CF27" :
            cm53 = camera_notification(id=27, CameraNoti_name='CAM027+Notification', CameraNoti_status='0' )
            cm53.save()

            #Add object into database
            d70 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบเจ็ด', daly_time=ticks )
            d70.save()


        elif var001 == "CO28" :
            cm54 = camera_notification(id=28, CameraNoti_name='CAM028+Notification', CameraNoti_status='1' )
            cm54.save()

            #Add object into database
            d71 = daily_feeds(daily_name='เปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบแปด', daly_time=ticks )
            d71.save()
        
        
        elif var001 == "CF28" :
            cm55 = camera_notification(id=28, CameraNoti_name='CAM028+Notification', CameraNoti_status='0' )
            cm55.save()

            #Add object into database
            d72 = daily_feeds(daily_name='ปิดการแจ้งเตือนของกล้องตัวที่ยี่สิบแปด', daly_time=ticks )
            d72.save()






        if form.is_valid():
            text = form.cleaned_data['post']          


        args = {'var12': header_str, 'posts': posts, 'posts2': posts2, 'posts3' : posts3, 'posts5' : posts5, 'posts6' : posts6, 'posts8' : posts8, 'posts9' : posts9, 'posts10' : posts10, 'posts12' : posts12, 'posts14' : posts14, 'posts16' : posts16, 'posts18' : posts18, 'posts20' : posts20, 'posts22' : posts22, 'posts24' : posts24, 'posts26' : posts26, 'posts28' : posts28, 'posts30' : posts30, 'posts32' : posts32, 'posts34' : posts34, 'posts36' : posts36, 'posts38' : posts38, 'posts40' : posts40, 'posts42' : posts42, 'posts44' : posts44, 'posts46' : posts46, 'posts48' : posts48, 'posts50' : posts50, 'posts52' : posts52, 'posts54' : posts54, 'posts56' : posts56, 'posts58' : posts58,'posts60' : posts60,'posts62' : posts62,'posts64' : posts64, 'posts66' : posts66, 'posts68' : posts68, 'posts70' : posts70, 'posts72' : posts72, 'posts74' : posts74, 'posts76' : posts76, 'posts78' : posts78, 'postsD' : postsD, 'posts80' : posts80, 'posts82' : posts82, 'posts84' : posts84, 'posts86' : posts86, 'posts88' : posts88, 'posts90' : posts90, 'posts92' : posts92, 'posts94' : posts94, 'posts96' : posts96, 'posts98' : posts98, 'posts100' : posts100, 'posts102' : posts102, 'posts104' : posts104, 'posts106' : posts106, 'posts108' : posts108, 'posts110' : posts110, 'posts112' : posts112, 'posts114' : posts114, 'posts116' : posts116, 'posts118' : posts118, 'posts120' : posts120, 'posts122' : posts122, 'posts124' : posts124, 'posts126' : posts126, 'posts128' : posts128, 'posts130' : posts130, 'posts132' : posts132, 'posts134' : posts134    }
        return redirect('http://127.0.0.1:8000/mainpage/')


def test12(request) :
    template = loader.get_template('test12.html')
    header_str = 'Test modal pop up'

    args = {'var12': header_str}

    return HttpResponse(template.render(args, request))

class ChangeStatus(View) :
    template_name = 'test13.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
           
        Overnam = request.POST['Over_name']
        Overnum = request.POST['Over_num']
        form = HomeForm(request.POST)
    

        b4 = overviewStatus(id=1, Over_name=Overnam, Over_num=Overnum )
        b4.save()


        if form.is_valid():
            text = form.cleaned_data['post']   
       
      
       
        args = {'form': form}
        return render(request,self.template_name, args)



def test14(request) :
    template = loader.get_template('test14.html')
    header_str = 'Test modal image pop up'

    args = {'var14': header_str}

    return HttpResponse(template.render(args, request))

class ChangeStatus2(View) :
    template_name = 'test15.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum1 = request.POST['IPnum1']
        IPconnect1 = request.POST['IPconnect1']
        IPODconnect1 = request.POST['IPODconnect1']

        form = HomeForm(request.POST)
        #add object into database
    

        #Edit object into database

        b6 = IPstatus(id=1, IPnum=IPnum1, IPconnect=IPconnect1, IP_ODconnect=IPODconnect1 )
        b6.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)

class ChangeStatus2_2(View) :
    template_name = 'test16.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum2 = request.POST['IPnum2']
        IPconnect2 = request.POST['IPconnect2']
        IPODconnect2 = request.POST['IPODconnect2']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b8 = IPstatus(id=2, IPnum=IPnum2, IPconnect=IPconnect2, IP_ODconnect=IPODconnect2 )
        b8.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)

class ChangeStatus3(View) :
    template_name = 'test17.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum3 = request.POST['IPnum3']
        IPconnect3 = request.POST['IPconnect3']
        IPODconnect3 = request.POST['IPODconnect3']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b10 = IPstatus(id=3, IPnum=IPnum3, IPconnect=IPconnect3, IP_ODconnect=IPODconnect3 )
        b10.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)

class ChangeStatus4(View) :
    template_name = 'test18.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum4 = request.POST['IPnum4']
        IPconnect4 = request.POST['IPconnect4']
        IPODconnect4 = request.POST['IPODconnect4']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b11 = IPstatus(id=4, IPnum=IPnum4, IPconnect=IPconnect4, IP_ODconnect=IPODconnect4 )
        b11.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus5(View) :
    template_name = 'test19.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum5 = request.POST['IPnum5']  
        IPconnect5 = request.POST['IPconnect5']
        IPODconnect5 = request.POST['IPODconnect5']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b12 = IPstatus(id=5, IPnum=IPnum5, IPconnect=IPconnect5, IP_ODconnect=IPODconnect5 )
        b12.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus6(View) :
    template_name = 'test20.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum6 = request.POST['IPnum6']
        IPconnect6 = request.POST['IPconnect6']
        IPODconnect6 = request.POST['IPODconnect6']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b13 = IPstatus(id=6, IPnum=IPnum6, IPconnect=IPconnect6, IP_ODconnect=IPODconnect6 )
        b13.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus7(View) :
    template_name = 'test21.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum7 = request.POST['IPnum7']
        IPconnect7 = request.POST['IPconnect7']
        IPODconnect7 = request.POST['IPODconnect7']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b14 = IPstatus(id=7, IPnum=IPnum7, IPconnect=IPconnect7, IP_ODconnect=IPODconnect7 )
        b14.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus8(View) :
    template_name = 'test22.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum8 = request.POST['IPnum8']
        IPconnect8 = request.POST['IPconnect8']
        IPODconnect8 = request.POST['IPODconnect8']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b15 = IPstatus(id=8, IPnum=IPnum8, IPconnect=IPconnect8, IP_ODconnect=IPODconnect8 )
        b15.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus9(View) :
    template_name = 'test23.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum9 = request.POST['IPnum9']
        IPconnect9 = request.POST['IPconnect9']
        IPODconnect9 = request.POST['IPODconnect9']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b15 = IPstatus(id=9, IPnum=IPnum9, IPconnect=IPconnect9, IP_ODconnect=IPODconnect9 )
        b15.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus10(View) :
    template_name = 'test24.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum10 = request.POST['IPnum10']
        IPconnect10 = request.POST['IPconnect10']
        IPODconnect10 = request.POST['IPODconnect10']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b16 = IPstatus(id=10, IPnum=IPnum10, IPconnect=IPconnect10, IP_ODconnect=IPODconnect10 )
        b16.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus11(View) :
    template_name = 'test25.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum11 = request.POST['IPnum11']
        IPconnect11 = request.POST['IPconnect11']
        IPODconnect11 = request.POST['IPODconnect11']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b17 = IPstatus(id=11, IPnum=IPnum11, IPconnect=IPconnect11, IP_ODconnect=IPODconnect11 )
        b17.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)

class ChangeStatus12(View) :
    template_name = 'test26.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum12 = request.POST['IPnum12']
        IPconnect12 = request.POST['IPconnect12']
        IPODconnect12 = request.POST['IPODconnect12']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b18 = IPstatus(id=12, IPnum=IPnum12, IPconnect=IPconnect12, IP_ODconnect=IPODconnect12 )
        b18.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)

class ChangeStatus13(View) :
    template_name = 'test27.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum13 = request.POST['IPnum13']
        IPconnect13 = request.POST['IPconnect13']
        IPODconnect13 = request.POST['IPODconnect13']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b19 = IPstatus(id=13, IPnum=IPnum13, IPconnect=IPconnect13, IP_ODconnect=IPODconnect13 )
        b19.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)



class ChangeStatus14(View) :
    template_name = 'test28.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum14 = request.POST['IPnum14']
        IPconnect14 = request.POST['IPconnect14']
        IPODconnect14 = request.POST['IPODconnect14']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b20 = IPstatus(id=14, IPnum=IPnum14, IPconnect=IPconnect14, IP_ODconnect=IPODconnect14 )
        b20.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)

class ChangeStatus15(View) :
    template_name = 'test29.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum15 = request.POST['IPnum15']
        IPconnect15 = request.POST['IPconnect15']
        IPODconnect15 = request.POST['IPODconnect15']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b21 = IPstatus(id=15, IPnum=IPnum15, IPconnect=IPconnect15, IP_ODconnect=IPODconnect15 )
        b21.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus16(View) :
    template_name = 'test30.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum16 = request.POST['IPnum16']
        IPconnect16 = request.POST['IPconnect16']
        IPODconnect16 = request.POST['IPODconnect16']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b22 = IPstatus(id=16, IPnum=IPnum16, IPconnect=IPconnect16, IP_ODconnect=IPODconnect16 )
        b22.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus17(View) :
    template_name = 'test31.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum17 = request.POST['IPnum17']
        IPconnect17 = request.POST['IPconnect17']
        IPODconnect17 = request.POST['IPODconnect17']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b23 = IPstatus(id=17, IPnum=IPnum17, IPconnect=IPconnect17, IP_ODconnect=IPODconnect17 )
        b23.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)

class ChangeStatus18(View) :
    template_name = 'test32.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum18 = request.POST['IPnum18']
        IPconnect18 = request.POST['IPconnect18']
        IPODconnect18 = request.POST['IPODconnect18']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b24 = IPstatus(id=18, IPnum=IPnum18, IPconnect=IPconnect18, IP_ODconnect=IPODconnect18 )
        b24.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)
    
class ChangeStatus19(View) :
    template_name = 'test33.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum19 = request.POST['IPnum19']
        IPconnect19 = request.POST['IPconnect19']
        IPODconnect19 = request.POST['IPODconnect19']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b25 = IPstatus(id=19, IPnum=IPnum19, IPconnect=IPconnect19, IP_ODconnect=IPODconnect19 )
        b25.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)

class ChangeStatus20(View) :
    template_name = 'test34.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum20 = request.POST['IPnum20']
        IPconnect20 = request.POST['IPconnect20']
        IPODconnect20 = request.POST['IPODconnect20']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b26 = IPstatus(id=20, IPnum=IPnum20, IPconnect=IPconnect20, IP_ODconnect=IPODconnect20 )
        b26.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus21(View) :
    template_name = 'test35.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum21 = request.POST['IPnum21']
        IPconnect21 = request.POST['IPconnect21']
        IPODconnect21 = request.POST['IPODconnect21']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b26 = IPstatus(id=20, IPnum=IPnum20, IPconnect=IPconnect20, IP_ODconnect=IPODconnect20 )
        b26.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)

class ChangeStatus22(View) :
    template_name = 'test36.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum22 = request.POST['IPnum22']
        IPconnect22 = request.POST['IPconnect22']
        IPODconnect22 = request.POST['IPODconnect22']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b27 = IPstatus(id=22, IPnum=IPnum22, IPconnect=IPconnect22, IP_ODconnect=IPODconnect22 )
        b27.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)

class ChangeStatus23(View) :
    template_name = 'test37.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum23 = request.POST['IPnum23']
        IPconnect23 = request.POST['IPconnect23']
        IPODconnect23 = request.POST['IPODconnect23']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b28 = IPstatus(id=23, IPnum=IPnum23, IPconnect=IPconnect23, IP_ODconnect=IPODconnect23 )
        b28.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus24(View) :
    template_name = 'test38.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum24 = request.POST['IPnum24']
        IPconnect24 = request.POST['IPconnect24']
        IPODconnect24 = request.POST['IPODconnect24']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b29 = IPstatus(id=24, IPnum=IPnum24, IPconnect=IPconnect24, IP_ODconnect=IPODconnect24 )
        b29.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus25(View) :
    template_name = 'test39.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum25 = request.POST['IPnum25']
        IPconnect25 = request.POST['IPconnect25']
        IPODconnect25 = request.POST['IPODconnect25']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b30 = IPstatus(id=25, IPnum=IPnum25, IPconnect=IPconnect25, IP_ODconnect=IPODconnect25 )
        b30.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus26(View) :
    template_name = 'test40.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum26 = request.POST['IPnum26']
        IPconnect26 = request.POST['IPconnect26']
        IPODconnect26 = request.POST['IPODconnect26']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b31 = IPstatus(id=26, IPnum=IPnum26, IPconnect=IPconnect26, IP_ODconnect=IPODconnect26 )
        b31.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus27(View) :
    template_name = 'test41.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum27 = request.POST['IPnum27']
        IPconnect27 = request.POST['IPconnect27']
        IPODconnect27 = request.POST['IPODconnect27']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b32 = IPstatus(id=27, IPnum=IPnum27, IPconnect=IPconnect27, IP_ODconnect=IPODconnect27 )
        b32.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeStatus28(View) :
    template_name = 'test42.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        IPnum28 = request.POST['IPnum28']
        IPconnect28 = request.POST['IPconnect28']
        IPODconnect28 = request.POST['IPODconnect28']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b33 = IPstatus(id=28, IPnum=IPnum28, IPconnect=IPconnect28, IP_ODconnect=IPODconnect28 )
        b33.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class Error_message(View) :
    template_name = 'test43.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))

        # current date and time
        now = datetime.now()
        ticks = now.strftime("%d/%m/%Y, %H:%M:%S")
    
        Error_mes = request.POST['ErrorTime']
        Error_ID = request.POST['ErrorID']
        Error_Name = request.POST['ErrorName']
        Error_detail = request.POST['ErrorDetail']

        form = HomeForm(request.POST)
    
        #add object into database
        b111 = Errormessage(errorID=Error_ID,errorName=Error_Name, errorTime=Error_mes, errorDetail=Error_detail)
        b111.save()

        d33 = daily_feeds(daily_name='ระบบตรวจจับผู้บุกรุกผิดพลาด: ' + ErrorName, daly_time=ticks )
        d33.save()


        #Edit object into database
        #b20 = IPstatus(id=5, IPnum=IPnum5, IPconnect=IPconnect5, IP_ODconnect=IPODconnect5 )
        #b20.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class ChangeMode(View) :
    template_name = 'test44.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
    
        Mode_Status = request.POST['ModeStatus']
        Mode_num = request.POST['ModeNum']

        form = HomeForm(request.POST)
    

        #Edit object into database

        b101 = overviewStatus(id=1, Over_name=Mode_Status, Over_num=Mode_num )
        b101.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
        
      
       
        args = {'form': form}
        return render(request,self.template_name, args)


class SPC_001(View) :
    template_name = 'test47.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))
        post_intru = Intruder.objects.all()
        last_blanck = "                         "
        last_End = "  ------ End ------  "
        # current date and time
        now = datetime.now()
        ticks = now.strftime("%d/%m/%Y, %H:%M:%S")


        #Filter_Feature_Variables

        #Human_filter
        filter_a = overviewStatus.objects.get(id=6)
        filter_b = filter_a.Over_num

        #CAT_filter
        filter_c = overviewStatus.objects.get(id=7)
        filter_d = filter_c.Over_num

        #Snake_filter
        filter_e = overviewStatus.objects.get(id=8)
        filter_f = filter_e.Over_num

        for intruder in post_intru:
            #print(intruder.Intru, "--", intruder.IPcam)
            last_Intru = request.POST['Intruder'] 
            last_IPcam = request.POST['Ipcamera'] 
            last_Time = request.POST['Time'] 
            last_Image = request.POST['ImageID'] 
        form = HomeForm(request.POST)
        #add object into database
        b2 = Intruder(Intru=last_Intru,IPcam=last_IPcam, Time=last_Time, ImageID=last_Image)
        b2.save()

        d2 = daily_feeds(daily_name='ระบบตรวจจับผู้บุกรุกเป็น: ' + last_Intru, daly_time=ticks )
        d2.save()

        #line_text = TestLine.line_text(last_Intru)
        #line_text = TestLine.line_text(last_IPcam)
        #line_text = TestLine.line_text(last_Time)
        #line_text = TestLine.line_text(last_Image)

        if filter_b == '1' and last_Intru == 'Human':
        
            line_pic = TestLine.line_pic(last_IPcam ,'C:/Users/Gain/Desktop/NewEGAT/results/'+ last_Image)
            line_text = TestLine.line_text(last_End)


        elif filter_d == '1' and last_Intru == 'Cat&Dog':
        
            line_pic = TestLine.line_pic(last_IPcam ,'C:/Users/Gain/Desktop/NewEGAT/results/' + last_Image)
            line_text = TestLine.line_text(last_End)

        elif filter_f == '1' and last_Intru == 'Snake':
        
            line_pic = TestLine.line_pic(last_IPcam ,'C:/Users/Gain/Desktop/NewEGAT/results/' + last_Image)
            line_text = TestLine.line_text(last_End)


        #line_text = TestLine.line_text(last_Intru)
        #line_text = TestLine.line_text(last_IPcam)
        #line_text = TestLine.line_text(last_Time)
        #line_text = TestLine.line_text(last_Image)
        #line_pic = TestLine.line_pic("Test", last_Image)

        #Edit object into database

        #b4 = overviewStatus(id=3, IPnum='CAM003',IPcam='Not123', Time='Not123', ImageID='Not123')
        #b4.save()

        #Delete object into database
        #Intruder.objects.filter(id=1).delete()


        if form.is_valid():
            text = form.cleaned_data['post']   
            print(line_pic)
            print(line_text)
       
        args = {'form': form}
        return render(request,self.template_name, args)


    

