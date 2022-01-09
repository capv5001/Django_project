from django.shortcuts import render

# Create your views here.Z
def blog(request):
    return render(request,'blog/blog.html')