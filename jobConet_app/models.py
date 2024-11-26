from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User 
class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona con el usuario autenticado
    fecha_creacion = models.DateTimeField(default=now)

    def __str__(self):
        return self.titulo
    
class OfertaEmpleo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
class BusquedaTrabajo(models.Model):
    palabra_clave = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    fecha_busqueda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.palabra_clave} - {self.ubicacion}"