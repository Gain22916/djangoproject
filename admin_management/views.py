from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request) :
    header_str = 'admin management : EGAT project'
    template = loader.get_template('index.html')
    context = {
        'var1' : header_str
    }
    return HttpResponse(template.render(context, request))

def line(request) :
    header_str = 'Line API management : EGAT project'
    template = loader.get_template('line.html')
    context = {
        'var1' : header_str
    }
    return HttpResponse(template.render(context, request))
