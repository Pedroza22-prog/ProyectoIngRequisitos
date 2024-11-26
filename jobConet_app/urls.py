from django.urls import path
from . import views  # Importar las vistas

urlpatterns = [
    path('', views.home, name='home'),  # Ruta principal
    path('agregar/', views.agregar_publicacion, name='agregar_publicacion'),  # Agregar publicación
    path('buscar/', views.oportunidades, name='oportunidades'),  # Buscar oportunidades
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),  # Eliminar publicación
    path('buscar-empleo/', views.buscar_empleo, name='buscar_empleo'),  # Buscar empleo
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),  # Actualizar publicación
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),  # Registrar usuario
    path('publicaciones/', views.lista_publicaciones, name='lista_publicaciones'),  # Listar publicaciones
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),  # Perfil del usuario
    path('editar/', views.editar_perfil, name='editar_perfil'),  # Editar perfil
]
