from django.shortcuts import render, HttpResponse

# Create your views here.

def app_two(request):
    return HttpResponse('<h1>app two</h1>')