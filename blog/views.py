from django.shortcuts import render
from blog.models import Categoria,Post

# Create your views here.Z
def Blog(request):
    
    lista_categorias=Categoria.objects.all()
    lista_posts=Post.objects.all()
    
    return render(request,'blog/blog.html',{
        'categorias':lista_categorias,
        'posts':lista_posts,
    })

def VistaCategoria(request, categoria_id):
    
    obtener_categoria=Categoria.objects.get(id=categoria_id)
    filtrar_posts=Post.objects.filter(categoria=obtener_categoria) # Here, filter products for categoria_id
    
    return render(request,'blog/categorias.html',{
        'categorias':obtener_categoria,
        'posts':filtrar_posts,
    })