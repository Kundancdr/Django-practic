from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def testpaper(request):
   que=" Who developed python?"
   a="Denis Riichie"
   b="Guido van Rossum"
   c="Ken Thomson"
   d="Bjarne Stroustrup"
   context={
       'que':que,
       'a':a,
       'b':b,
       'c':c,
       'd':d
   }
   template = loader.get_template('testpaper.html')
   res=template.render(context,request)
   return HttpResponse(res)

def result(request):
    s2= "<h1> hello it's result section inside examapp </h1>"
    return HttpResponse(s2)
