from django.shortcuts import render, HttpResponse

# Create your views here.

def app_one(request):
    return HttpResponse('<h1>app one</h1>')