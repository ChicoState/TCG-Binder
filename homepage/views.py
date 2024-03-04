from django.shortcuts import render
from django.http import HttpResponse

def splash(request):
    return render(request, 'splash.html')
