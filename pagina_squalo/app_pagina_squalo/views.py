from django.shortcuts import render, redirect
from . forms import UsuarioForm

# Create your views here.


def home(request):
    return render (request, "home.html")


def formulario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias') 
    else:
        form = UsuarioForm()
    return render(request,"formulario.html",{"form":form})

def gracias_inscripcion(request):
    return render(request, "gracias.html")

def sobre_nosotros(request):
    return render(request, "sobre_nosotros.html")

def proyectos(request):
    return render(request, "proyectos.html")

def noticias(request):
    return render(request, "noticias.html")

def galeria(request):
    return render(request, "galeria.html")

def unete(request):
    return render(request, "unete.html")

def patrocinios(request):
    return render(request, "patrocinios.html")

def contacto(request):
    return render(request, "contactanos.html")