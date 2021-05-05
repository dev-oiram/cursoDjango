from django.db import models

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre Autor', max_length=50, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=50, blank=False,null=False)
    nacionalidad = models.CharField('Nacionalidad', max_length=50, blank=False, null=False)

    class Meta:
        verbose_name='Autor'
        verbose_name_plural= 'Autores'

    def __str__(self):
        return self.nombre + " "+self.apellidos

class Publicaciones(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=50,blank=True,null=False)
    fecha_publicacion = models.DateField('Fecha de Publicación', auto_now=True, auto_now_add=False)
    fecha_modificacion = models.DateField('Fecha de Modificación', auto_now=False, auto_now_add=True)
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Publicación'
        verbose_name_plural= 'Publicaciones'

    def __str__(self):
        return self.titulo