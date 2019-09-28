from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def test(request) :
    header_str = 'Test management'
    template = loader.get_template('test.html')
    context = {
        'var1' : header_str
    }
    return HttpResponse(template.render(context, request))