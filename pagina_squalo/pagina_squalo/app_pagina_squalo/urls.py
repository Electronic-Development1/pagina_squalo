from django.urls import path
from app_pagina_squalo import views

urlpatterns = [

    path("",views.home, name = "home"),
    path("sobre_nosotros/",views.sobre_nosotros, name = "sobre_nosotros"),
    path("formulario/", views.formulario, name = "formulario") ,
    path("proyectos/", views.proyectos, name = "proyectos") ,
    path("noticias/", views.noticias, name = "notocias") ,
    path("galeria/", views.galeria, name = "galeria") ,
    path("unete/", views.unete, name = "unete") ,
    path("patrocinios/", views.patrocinios, name = "patrocinios") ,
    path("contactanos/", views.contacto, name = "contactanos") ,
    
    path("gracias/",views.gracias_inscripcion, name = "gracias"),
]