from django import forms
from .models import Autor,Publicaciones

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad']
    
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['titulo','autor_id']