from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Function1_app1(request):
    return HttpResponse("<h1><i>Hi i am Function1 in app1</i></h1>")

def Function2_app1(request):
    return HttpResponse("Hi i am Function2 in app2")