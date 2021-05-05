from django.urls import path
from .views import crearAutor,listarAutores, editarAutores, eliminarAutor


urlpatterns = [
    path("crear_autor/", crearAutor, name="crear_autor"),
    path("listar_autores/", listarAutores, name="listar_autores"),
    path('actualizar_autor/<int:id>', editarAutores , name='actualizar_autor'),
    path('eliminar_autor/<int:id>', eliminarAutor , name='eliminar_autor'),
]
