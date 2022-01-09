from django.shortcuts import render
from blog.models import Categoria,Post

# Create your views here.Z
def blog(request):
    categorias=Categoria.objects.all()
    posts=Post.objects.all()
    return render(request,'blog/blog.html',{
        'categorias':categorias,
        'posts':posts,
    })