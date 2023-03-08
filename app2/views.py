from django.shortcuts import render
 
from django.http import HttpResponse
# Create your views here.

def Function1_app2(request):
    return HttpResponse("<h1> Hi i am Function1 in app2</h1>")

def Function2_app2(request):
    return HttpResponse("<marquee><i><h1>Hi i am Function2 in app2</h1></i></marquee>")