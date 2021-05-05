from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Autor
from .forms import AutorForm
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