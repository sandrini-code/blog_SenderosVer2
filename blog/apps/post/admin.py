from django.contrib import admin
from .models import *


# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    ordering= ('id', 'nombre', 'activado', 'fecha_creacion')
    search_files=('id', 'nombre', 'activado', 'fecha_creacion')
    list_display= ('id', 'nombre', 'activado', 'fecha_creacion')
    list_filter=('activado',)

class PostAdmin(admin.ModelAdmin):
    ordering= ('id', 'titulo', 'categoria', 'publicado', 'fecha_creacion', 'usuario')
    search_files=('id', 'titulo', 'categoria__nombre', 'publicado', 'fecha_creacion')
    list_display= ('id', 'titulo', 'categoria', 'publicado', 'fecha_creacion', 'usuario')
    list_filter=('categoria__nombre', 'publicado', 'usuario')
class ComentarioAdmin(admin.ModelAdmin):
    ordering = ('usuario', 'texto', 'posteo', 'fecha')
    search_fields = ('usuario__nombre', 'texto', 'posteo', 'fecha')
    list_display = ('usuario', 'texto', 'posteo', 'fecha')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)
