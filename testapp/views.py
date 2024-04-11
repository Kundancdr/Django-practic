from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def greeting(request):
    s="hello it's my sec project"
    return HttpResponse(s)

def about(request):
  template = loader.get_template('about.html')
  res=template.render()
  return HttpResponse(res)

def contact(request):
    s2= "<h1> hello it's contact section inside testapp </h1>"
    return HttpResponse(s2)