from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Simple
from django.http import HttpResponse


# Create your views here.

def test(request) :
    header_str = 'Test management 123'
    queryset = Simple.objects.all()
    context = {
        'var1' : queryset
        #'var2' : queryset
    }
    
    return render(request,'test.html', context)
