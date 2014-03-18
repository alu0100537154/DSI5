from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
  return HttpResponse("esto es home")

def about(request):
  return HttpResponse("esto es about")

def help(request):
  return HttpResponse("esto es help")

