from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class InstitucionForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    direccion = forms.CharField(max_length=60, required=True) #CharField si queremos ingresar un texto #IntegerField para que sea numerico
    

class PosicionForm(forms.Form):
    equipo = forms.CharField(max_length=60, required=True)
    puntos = forms.IntegerField(required=True)
    
class GoleadorForm(forms.Form):
    nombre = forms.CharField(max_length=60, required=True)
    goles =  forms.IntegerField(required=True)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
    
class FixtureForm(forms.Form):
    local = forms.CharField(max_length=100)
    vs = forms.CharField(max_length=100)
    visitante = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100) 

    

