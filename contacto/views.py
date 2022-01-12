from django import forms
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .forms import FormularioContacto
# Create your views here.

def contacto(request):

    if request.method=='POST':
        formulario_contacto=FormularioContacto(request.POST)
        
        if formulario_contacto.is_valid():
            data=formulario_contacto.cleaned_data
            
            send_mail(
                data['nombre'],
                data['contenido'],
                data.get('email',''),
                ['capv5001@gmail.com']
                )
            
            return redirect('contacto/contacto/?valido')

    else:
        formulario_contacto=FormularioContacto()

    return render(request,'contacto/contacto.html',{
        'formulario':formulario_contacto
    })