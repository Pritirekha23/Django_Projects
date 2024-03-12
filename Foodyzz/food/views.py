from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("HELLO WORLD")

def item(request):
    return HttpResponse("<h1>Hii PRITIREKHA</h1>")