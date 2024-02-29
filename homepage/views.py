from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse("Homepage Index")

def homepage(request):
    return render(request, 'homepage/home.html')
