from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

#_menuprincipal

urlpatterns = [
    path('', home, name="home"),
 
    
    path('Posicion/', PosicionList.as_view(), name= "Posicion"),
    path("Posicion_create/", PosicionCreate.as_view(), name="Posicion_create"),
    path("Posicion_update/<int:pk>", PosicionUpdate.as_view(), name="Posicion_update"),
    path("Posicion_delete/<int:pk>", PosicionDelete.as_view(), name="Posicion_delete"),
    

    
    path('institucion/', InstitucionList.as_view(), name="Institucion"),
    path('Institucion_create/', InstitucionCreate.as_view(), name="Institucion_create"),
    path("Institucion_update/<int:pk>", InstitucionUpdate.as_view(), name="Institucion_update"),
    path("Institucion_delete/<int:pk>", InstitucionDelete.as_view(), name="Institucion_delete"),


    
    path('acerca/', acerca, name="acerca_de_mi"),
    path('buscar_institucion/', buscarInstitucion, name="buscar_institucion"),
    path('encontrar_Institucion/', encontrarInstitucion, name="encontrar_institucion"),
    path('buscar_posicion/', buscarPosicion, name="buscar_posicion"),
    path('encontrar_posicion/', encontrarPosicion, name="encontrar_posicion"),
 
    
    path('institucion_form/', institucionForm, name="Institucion_form"),
    path('posicionForm/', posicionForm, name="Posicion_form"),
    

    path('buscar_goleador/', buscarGoleador, name="buscar_goleador"),
    path('encontrar_goleador/', encontrarGoleador, name="encontrar_goleador"),

    path('goleador/', GoleadorList.as_view(), name="goleadores"),
    path('Goleador_create/', GoleadorCreate.as_view(), name="Goleador_create"),
    path('Goleador_update/<int:pk>', GoleadorUpdate.as_view(), name="Goleador_update"),
    path('Goleador_delete/<int:pk>', GoleadorDelete.as_view(), name="Goleador_delete"),

    path('fixtures/', FixtureList.as_view(), name="fixtures"),
    path('fixture_create/', FixtureCreate.as_view(), name="fixture_create"),
    path('fixture_update/<int:pk>', FixtureUpdate.as_view(), name="fixture_update"),
    path('fixture_delete/<int:pk>', FixtureDelete.as_view(), name="fixture_delete"),
    path('buscar_fixture/', buscarFixture, name="buscar_fixture"),
    path('encontrar_fixture/', encontrarFixture, name="encontrar_fixture"),

    
    
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('registrar/', register, name ="registrar"),
    
    
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar', agregarAvatar, name="agregar_avatar"),
    
    
    
    
    
]