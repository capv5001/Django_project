from django.shortcuts import render,HttpResponse
from websiteApp import urls


# Create your views here.

def home(request):
    return render(request,'websiteApp/home.html')

def tienda(request):
    return render(request,'websiteApp/tienda.html')

def blog(request):
    menu_link=urls.urlpatterns
    return render(request,'websiteApp/blog.html',{
        'link':menu_link
    })

def contacto(request):
    return render(request,'websiteApp/contacto.html')