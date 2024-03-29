from django.shortcuts import render, redirect
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test

def es_admin(user):
    return user.is_superuser


# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def acerca(request):
    return render(request, "aplicacion/acerca.html")

#_____________
@login_required
def buscarInstitucion(request):
    return render(request, "aplicacion/buscar.html")

@login_required
def encontrarInstitucion(request):
    buscar_query = request.GET.get("buscar", None)
    if buscar_query:
        instituciones = Institucion.objects.filter(nombre__icontains=buscar_query)
    else:
        instituciones = Institucion.objects.all()
    
    contexto = {"institucion": instituciones}
    return render(request, "aplicacion/Institucion.html", contexto)

@login_required
def buscarPosicion(request):
    return render(request, "aplicacion/buscarposicion.html")

@login_required
def encontrarPosicion(request):
    buscar_query = request.GET.get("buscar", None)
    if buscar_query:
        posiciones = Posicion.objects.filter(equipo__icontains=buscar_query)
    else:
        posiciones = Posicion.objects.all()
    
    contexto = {"posiciones": posiciones}
    return render(request, "aplicacion/Posicion.html", contexto)

@login_required
def buscarGoleador(request):
    return render(request, "aplicacion/buscargoleador.html")

@login_required
def encontrarGoleador(request):
    buscar_query = request.GET.get("buscar", None)
    if buscar_query:
        goleadores = Goleador.objects.filter(nombre__icontains=buscar_query)
    else:
        goleadores = Goleador.objects.all()
    
    contexto = {'goleadores': goleadores}
    return render(request, "aplicacion/goleadores.html", contexto)

@login_required    
def buscarFixture(request):
    return render(request, "aplicacion/buscarfixture.html")

@login_required
@login_required
def encontrarFixture(request):
    buscar_query = request.GET.get("buscar", None)
    if buscar_query:
        fixtures = Fixture.objects.filter(local__icontains=buscar_query) | Fixture.objects.filter(visitante__icontains=buscar_query)
    else:
        fixtures = Fixture.objects.all()
    
    contexto = {'fixtures': fixtures}
    return render(request, "aplicacion/fixtures.html", contexto)



#__forms
@login_required
def institucionForm(request):
    if request.method == "POST": 
        miForm = InstitucionForm(request.POST)
        if miForm.is_valid():
            institucion_nombre = miForm.cleaned_data.get("nombre")
            institucion_direccion = miForm.cleaned_data.get("direccion")
            institucion = Institucion(nombre=institucion_nombre, direccion=institucion_direccion)
            institucion.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = InstitucionForm()
        
    return render(request, "aplicacion/institucionForm.html", {"form": miForm} )

@login_required
def posicionForm(request):
    if request.method == "POST": 
        miForm = PosicionForm(request.POST)
        if miForm.is_valid():
            posicion_equipo = miForm.cleaned_data.get("equipo")
            posicion_puntos = miForm.cleaned_data.get("puntos")
            posicion = Posicion(nombre=posicion_equipo, direccion=posicion_puntos)
            posicion.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = PosicionForm()
        
    return render(request, "aplicacion/posicionForm.html", {"form": miForm} )

def login_request(request):
    if request.method == "POST": 
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url 
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            
            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))           
    else:
        miForm = AuthenticationForm()
        
    return render(request, "aplicacion/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST": 
        miForm = RegistroForm(request.POST)
        
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))           
    else:
        miForm = RegistroForm()
        
    return render(request, "aplicacion/registro.html", {"form": miForm} )

def goleadorCreate(request):
    if request.method == "POST":
        miForm = GoleadorForm(request.POST)
        if miForm.is_valid():
            goleador_nombre = miForm.cleaned_data.get("nombre")
            goleador_goles = miForm.cleaned_data.get("goles")
            goleador = Goleador(nombre=goleador_nombre, goles=goleador_goles)
            goleador.save()
            return render(request, "aplicacion/index.html")
    else:
        miForm = GoleadorForm()
        
    return render(request, "aplicacion/goleadorForm.html", {"form": miForm} )




#______ Institucion


class InstitucionList(LoginRequiredMixin, ListView):
    model = Institucion
    

class InstitucionCreate(LoginRequiredMixin, CreateView):
    model = Institucion
    fields = ["nombre", "direccion"]
    success_url = reverse_lazy("Institucion")

class InstitucionUpdate(LoginRequiredMixin, UpdateView):
    model = Institucion
    fields = ["nombre", "direccion"]
    success_url = reverse_lazy("Institucion")
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class InstitucionDelete(LoginRequiredMixin, DeleteView):
    model = Institucion
    success_url = reverse_lazy("Institucion")

class PosicionList(LoginRequiredMixin, ListView):
    model = Posicion

class PosicionCreate(LoginRequiredMixin, CreateView):
    model = Posicion
    fields = ["equipo", "puntos"]
    success_url = reverse_lazy("Posicion")
    
class PosicionUpdate(LoginRequiredMixin, UpdateView):
    model = Posicion
    fields = ["equipo", "puntos"]
    success_url = reverse_lazy("Posicion")

class PosicionDelete(LoginRequiredMixin, DeleteView):
    model = Posicion
    success_url = reverse_lazy("Posicion")
    

class GoleadorList(LoginRequiredMixin, ListView):
    model = Goleador
    
class GoleadorCreate(LoginRequiredMixin, CreateView):
    model = Goleador
    fields = ["nombre", "goles"]
    success_url = reverse_lazy("goleadores")
    
class GoleadorUpdate(LoginRequiredMixin, UpdateView):
    model = Goleador
    fields = ["nombre", "goles"]
    success_url = reverse_lazy("goleadores")
    
class GoleadorDelete(LoginRequiredMixin, DeleteView):
    model = Goleador
    success_url = reverse_lazy("goleadores")

class FixtureList(LoginRequiredMixin, ListView):
    model = Fixture
    
class FixtureCreate(LoginRequiredMixin, CreateView):
    model = Fixture
    fields = ["local", "vs", "visitante", "direccion"]
    success_url = reverse_lazy("fixtures")
    
class FixtureUpdate(LoginRequiredMixin, UpdateView):
    model = Fixture
    fields = ["local", "vs", "visitante", "direccion"]
    success_url = reverse_lazy("fixtures")
    
class FixtureDelete(LoginRequiredMixin, DeleteView):
    model = Fixture
    success_url = reverse_lazy("fixtures")

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")
    


#_____Edicion de Perfil

@login_required
def editProfile(request):
    usuario = request.user
    
    if request.method == "POST": 
        miForm = UserEditForm(request.POST, instance=usuario)
        
        if miForm.is_valid():
            miForm.save()
            return redirect('home')  # Usa el nombre de la URL directamente en la redirección
    else:
        miForm = UserEditForm(instance=usuario)
        
    return render(request, "aplicacion/editarPerfil.html", {"form": miForm} )

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
         
            #
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
                    
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            print(f"{imagen}")
            return redirect(reverse_lazy('home'))
        
    else:
        miForm = AvatarForm()
        
    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm} )