from django.contrib import admin
from .models import Publicacion, OfertaEmpleo, BusquedaTrabajo

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion')  # Columnas visibles en el administrador
    search_fields = ('titulo', 'contenido')  # Agrega búsqueda por título y contenido

@admin.register(OfertaEmpleo)
class OfertaEmpleoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ubicacion', 'fecha_publicacion')
    search_fields = ('titulo', 'descripcion', 'ubicacion')

@admin.register(BusquedaTrabajo)
class BusquedaTrabajoAdmin(admin.ModelAdmin):
    list_display = ('palabra_clave', 'ubicacion', 'fecha_busqueda')
    search_fields = ('palabra_clave', 'ubicacion')