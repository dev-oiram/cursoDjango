from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Autor, Publicaciones
from .forms import AutorForm, PublicacionForm

# Create your views here.
def Home(request):
    return render(request,'index.html')

def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
    return render(request,'aplicaciones/crear_autor.html',{'autor_form': autor_form})

def listarAutores(request):
    autores = Autor.objects.all()
    return render(request,'aplicaciones/listar_autores.html',{'nombresAutores': autores})

def editarAutores(request,id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id=id)
        if request.method == 'GET':
            autor_form = AutorForm(instance= autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
                return redirect('/publicaciones/listar_autores/')
    except ObjectDoesNotExist as e:
        error = e
    return render (request,'aplicaciones/actualizar_autor.html',{'autor_form': autor_form, 'error': error})
    
def eliminarAutor(request,id):
    autor = Autor.objects.get(id=id)
    if request.method == 'POST':
        autor.delete()
        return redirect('/publicaciones/listar_autores/')
    return render(request,'aplicaciones/eliminar_autor.html',{'autor': autor})


def crearPublicacion(request):
    if request.method == 'POST':
        publicacion_form = PublicacionForm(request.POST)
        print(request.POST)
        if publicacion_form.is_valid():
            publicacion_form.save()
            return redirect('index')
    else:
        publicacion_form = PublicacionForm()
    return render(request,'aplicaciones/crear_publicacion.html',{'publicacion_form': publicacion_form})

def listarPublicaciones(request):
    publicaciones = Publicaciones.objects.all()
    return render(request,'aplicaciones/listar_publicaciones.html',{'nombres_publicaciones': publicaciones})

def eliminarPublicacion(request,id):
    publicacion = Publicaciones.objects.get(id=id)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('/publicaciones/listar_publicaciones/')
    return render(request,'aplicaciones/eliminar_publicacion.html',{'publicacion': publicacion})

def editarPublicacion(request,id):
    publicacion_form = None
    error = None
    try:
        publicacion = Publicaciones.objects.get(id=id)
        if request.method == 'GET':
            publicacion_form = PublicacionForm(instance= publicacion)
        else:
            publicacion_form = PublicacionForm(request.POST, instance=publicacion)
            if publicacion_form.is_valid():
                publicacion_form.save()
                return redirect('/publicaciones/listar_publicaciones/')
    except ObjectDoesNotExist as e:
        error = e
    return render (request,'aplicaciones/actualizar_publicacion.html',{'publicacion_form': publicacion_form, 'error': error})