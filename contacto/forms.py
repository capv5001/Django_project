from django import forms
from django.forms.widgets import Textarea

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label='nombre',required=True)
    email=forms.EmailField(label='email',required=True)
    contenido=forms.CharField(label='contenido',widget=Textarea)