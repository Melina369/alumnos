from django.core import validators
from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import User

#Formulario de registro
class StudentRegistration(forms.ModelForm):
    class Meta:
        model= User
        fields=['name', 'email', 'password']
        widgets= {
            #controles de tipo de datos y estilo
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True ,attrs={'class':'form-control'})
        }