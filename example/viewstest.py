from django.shortcuts import render, redirect
from django.template import loader
from .models import Simple
from django.http import HttpResponse
from example.forms import HomeForm
from django.views import View
import requests
from admin_management import LineAPI
from example.models import Simple, Intruder, Errormessage, IPstatus,overviewStatus
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
        last_blanck = "                         "
        last_End = "  ------ End ------  "


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

        #line_text = TestLine.line_text(last_Intru)
        #line_text = TestLine.line_text(last_IPcam)
        #line_text = TestLine.line_text(last_Time)
        #line_text = TestLine.line_text(last_Image)

        if filter_b == '1' and last_Intru == 'HUMAN':
        
            line_pic = TestLine.line_pic(last_IPcam , last_Image)
            line_text = TestLine.line_text(last_End)


        elif filter_d == '1' and last_Intru == 'CAT':
        
            line_pic = TestLine.line_pic(last_IPcam , last_Image)
            line_text = TestLine.line_text(last_End)

        elif filter_f == '1' and last_Intru == 'SNAKE':
        
            line_pic = TestLine.line_pic(last_IPcam , last_Image)
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
    
    
    if posts3 == '1' and posts20 == '1' and posts22 == '1' and posts24 == '1' and posts26 == '1' and posts28 == '1' and posts30 == '1' and posts32 == '1' and posts34 == '1' and posts36 == '1' and posts38 == '1' and posts40 == '1' and posts42 == '1' and posts44 == '1' and posts46 == '1' and posts48 == '1' and posts50 == '1' and posts52 == '1' and posts54 == '1' and posts56 == '1' and posts58 == '1' and posts60 == '1' and posts62 == '1' and posts64 == '1' and posts66 == '1' and posts68 == '1' and posts70 == '1' and posts72 == '1' :
        #Edit object into database
        b10 = overviewStatus(id=2, Over_name='IPcameraConnection', Over_num='1' )
        b10.save()
        b11 = overviewStatus(id=3, Over_name='ODsystem', Over_num='1' )
        b11.save()
    else: 
        #Edit object into database
        b12 = overviewStatus(id=2, Over_name='IPcameraConnection', Over_num='0' )
        b12.save()
        b13 = overviewStatus(id=3, Over_name='ODsystem', Over_num='0' )
        b13.save()
    
    args = {'var12': header_str, 'posts': posts, 'posts2': posts2, 'posts3' : posts3, 'posts5' : posts5, 'posts6' : posts6, 'posts8' : posts8, 'posts9' : posts9, 'posts10' : posts10, 'posts12' : posts12, 'posts14' : posts14, 'posts16' : posts16, 'posts18' : posts18, 'posts20' : posts20, 'posts22' : posts22, 'posts24' : posts24, 'posts26' : posts26, 'posts28' : posts28, 'posts30' : posts30, 'posts32' : posts32, 'posts34' : posts34, 'posts36' : posts36, 'posts38' : posts38, 'posts40' : posts40, 'posts42' : posts42, 'posts44' : posts44, 'posts46' : posts46, 'posts48' : posts48, 'posts50' : posts50, 'posts52' : posts52, 'posts54' : posts54, 'posts56' : posts56, 'posts58' : posts58,'posts60' : posts60,'posts62' : posts62,'posts64' : posts64, 'posts66' : posts66, 'posts68' : posts68, 'posts70' : posts70, 'posts72' : posts72  }

    return HttpResponse(template.render(args, request))

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
    
        Error_mes = request.POST['ErrorTime']
        Error_ID = request.POST['ErrorID']
        Error_Name = request.POST['ErrorName']
        Error_detail = request.POST['ErrorDetail']

        form = HomeForm(request.POST)
    
        #add object into database
        b111 = Errormessage(errorID=Error_ID,errorName=Error_Name, errorTime=Error_mes, errorDetail=Error_detail)
        b111.save()


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


class Filter01(View) :
    
    template_name = 'test45.html'

    def get(self,request) :
        header_str = 'Post Method'
        form = HomeForm()
        args = {'form': form}
        return render(request,self.template_name, args)

    def post(self, request):
        print(type(request))

        form = HomeForm(request.POST)
        var001 = str(request.POST["Value1"])
       
        print(var001)

        if var001 == "G" :
            f01 = overviewStatus(id=6, Over_name='HumanFilter', Over_num='1' )
            f01.save()

        elif var001 == "H" :
            f02 = overviewStatus(id=6, Over_name='HumanFilter', Over_num='0' )
            f02.save()

        elif var001 == "I" :
            f03 = overviewStatus(id=7, Over_name='CatFilter', Over_num='1' )
            f03.save()
        
        elif var001 == "J" :
            f04 = overviewStatus(id=7, Over_name='CatFilter', Over_num='0' )
            f04.save()

        elif var001 == "K" :
            f05 = overviewStatus(id=8, Over_name='SnakeFilter', Over_num='1' )
            f05.save()

        elif var001 == "L" :
            f06 = overviewStatus(id=8, Over_name='SnakeFilter', Over_num='0' )
            f06.save()
    
            

        if form.is_valid():
            text = form.cleaned_data['post']          


        args = {'form': form}
        return render(request,self.template_name, args)

