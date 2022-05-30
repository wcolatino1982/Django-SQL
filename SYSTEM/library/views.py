from email.errors import InvalidMultipartContentTransferEncodingDefect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def nosotros(request):
    return render(request, 'pages/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    #print(libros)
    return render(request, 'libros/index.html', {'libros':libros})

def editLibros(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/edit.html', {'formulario':formulario})

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros') 

def createLibros(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/create.html', {'formulario':formulario})

def formLibros(request):
    return render(request, 'libros/form.html')
