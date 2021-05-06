from django.urls import path
from .views import crearAutor,listarAutores, editarAutores, eliminarAutor, crearPublicacion
from .views import listarPublicaciones, eliminarPublicacion, editarPublicacion


urlpatterns = [
    path("crear_autor/", crearAutor, name="crear_autor"),
    path("listar_autores/", listarAutores, name="listar_autores"),
    path('actualizar_autor/<int:id>', editarAutores , name='actualizar_autor'),
    path('eliminar_autor/<int:id>', eliminarAutor , name='eliminar_autor'),
    path("crear_publicacion/", crearPublicacion, name="crear_publicacion"),
    path("listar_publicaciones/", listarPublicaciones, name="listar_publicaciones"),
    path('eliminar_publicacion/<int:id>', eliminarPublicacion , name='eliminar_publicacion'),
    path('actualizar_publicacion/<int:id>', editarPublicacion , name='actualizar_publicacion'),
]
