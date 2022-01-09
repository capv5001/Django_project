from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'websiteApp/home.html')

def tienda(request):
    return render(request,'websiteApp/tienda.html')