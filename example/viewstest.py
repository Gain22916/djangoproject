from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Simple
from django.http import HttpResponse
from example.forms import HomeForm
from django.views import View
import requests
from admin_management import LineAPI
from example.models import Simple

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



 
