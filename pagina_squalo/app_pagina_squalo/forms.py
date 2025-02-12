from django import forms
from . models import Usuarios

class UsuarioForm(forms.ModelForm):
    class Meta: 
        model = Usuarios
        fields = [ 
            "nombre","telefono","email",
        ]

