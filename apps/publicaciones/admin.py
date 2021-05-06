from django.contrib import admin
from .models import Autor, Publicaciones
# Register your models here.
class autorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


admin.site.register(Autor, autorAdmin)
admin.site.register(Publicaciones)