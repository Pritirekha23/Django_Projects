from django.shortcuts import render,HttpResponse
from .models import Item

# Create your views here.

def index(request):
    item_list=Item.objects.all()
    return HttpResponse(item_list)

def item(request):
    return HttpResponse("<h1>Hii PRITIREKHA</h1>")