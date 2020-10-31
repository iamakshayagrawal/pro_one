from django.shortcuts import render, HttpResponse

# Create your views here.

def app_three(request):
    return HttpResponse('<h1>app three</h1>')