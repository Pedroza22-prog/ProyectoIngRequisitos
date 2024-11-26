from django.shortcuts import render, redirect
from .models import Publicacion
from django.shortcuts import render, redirect  # Importa funciones para renderizar plantillas y redirigir
from django.contrib.auth.models import User  # Modelo de usuario predeterminado de Django
from django.contrib.auth import login  # Función para iniciar sesión automáticamente después del registro
from django.contrib import messages  # Para mostrar mensajes de éxito o error al usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect
from django.contrib.auth import logout
from .forms import PublicacionForm  # Aquí se importa el formulario
from django.shortcuts import get_object_or_404, redirect
from .models import OfertaEmpleo
from .models import Publicacion, OfertaEmpleo, BusquedaTrabajo

#http://127.0.0.1:8000/
def home(request):
    """Vista para renderizar la página principal."""
    return render(request, 'jobConet_app/index.html')  # Renderiza el archivo index.html en la carpeta templates

def registrar_usuario(request):
    if request.method == 'POST':  # Verifica si el formulario se envió usando POST
        username = request.POST.get('username')  # Obtiene el nombre de usuario del formulario
        email = request.POST.get('email')  # Obtiene el correo electrónico del formulario
        password = request.POST.get('password')  # Obtiene la contraseña del formulario
        confirmar_password = request.POST.get('confirmar_password')  # Obtiene la confirmación de contraseña

        # Validar que las contraseñas coincidan
        if password != confirmar_password:  # Si las contraseñas no coinciden
            messages.error(request, "Las contraseñas no coinciden.")  # Envía un mensaje de error al usuario
            return redirect('registrar_usuario')  # Redirige de nuevo al formulario de registro

        # Intentar crear un nuevo usuario
        try:
            # create_user crea un usuario con nombre, email y contraseña en la base de datos
            usuario = User.objects.create_user(username=username, email=email, password=password)
            usuario.save()  # Guarda el usuario en la base de datos
            login(request, usuario)  # Inicia sesión automáticamente al usuario recién registrado
            messages.success(request, "Usuario registrado exitosamente.")  # Envía un mensaje de éxito
            return redirect('lista_publicaciones')  # Redirige al usuario a la lista de publicaciones
        except Exception as e:  # Captura cualquier error que ocurra durante el registro
            messages.error(request, f"Error al registrar usuario: {e}")  # Envía un mensaje de error con el detalle
            return redirect('registrar_usuario')  # Redirige al formulario de registro

    # Si el método es GET, muestra el formulario de registro
    return render(request, 'jobConet_app/registro.html')  # Renderiza la plantilla del formulario


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Iniciar sesión al usuario
            auth_login(request, form.get_user())
            next_url = request.GET.get('next', '/')  # Redirigir a la URL deseada después del login
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'jobConet_app/login.html', {'form': form})  # Ruta a tu plantilla personalizad

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige a la página de login (asegúrate de que 'login' esté definido en urls.py)

@login_required
def agregar_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            # Asigna el autor como el usuario que está actualmente autenticado
            publicacion.autor = request.user
            publicacion.save()
            messages.success(request, "¡Publicación agregada con éxito!")
            return redirect('lista_publicaciones')
        else:
            messages.error(request, "Hubo un error al agregar la publicación.")
    else:
        form = PublicacionForm()

    return render(request, 'jobConet_app/agregar_publicacion.html', {'form': form})

@login_required
def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')  # Evita duplicados con .distinct() si es necesario
    return render(request, 'jobConet_app/listar_publicaciones.html', {'publicaciones': publicaciones})

@login_required
def delete_post(request, post_id):
    publicacion = get_object_or_404(Publicacion, pk=post_id)

    # Verificamos si el usuario autenticado es el autor de la publicación
    if request.user == publicacion.autor:
        if request.method == 'POST':
            # Si es una petición POST, eliminamos la publicación
            publicacion.delete()
            # Redirigimos a la página que lista las publicaciones
            return redirect('lista_publicaciones')  # Redirige a la vista de lista_publicaciones
    
    # Si no se realiza la eliminación, renderizamos la página de confirmación
    return render(request, 'jobConet_app/confirm_delete.html', {'publicacion': publicacion})
    
    
@login_required
def update_post(request, post_id):
    publicacion = get_object_or_404(Publicacion, pk=post_id)

    # Verifica si el usuario autenticado es el autor de la publicación
    if request.user != publicacion.autor:
        messages.error(request, "No tienes permiso para editar esta publicación.")
        return redirect('lista_publicaciones')

    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Publicación actualizada con éxito!")
            return redirect('lista_publicaciones')
        else:
            messages.error(request, "Hubo un error al actualizar la publicación.")
    else:
        form = PublicacionForm(instance=publicacion)

    return render(request, 'jobConet_app/editar_publicacion.html', {'form': form, 'publicacion': publicacion})

@login_required
def perfil_usuario(request):
    usuario = request.user  # Obtiene el usuario autenticado
    return render(request, 'jobConet_app/perfil_usuario.html', {'usuario': usuario})

def home(request):
    """Vista para renderizar la página principal."""
    return render(request, 'jobConet_app/index.html')  # Renderiza el archivo index.html

def oportunidades(request):
    return render(request, "jobConet_app/oportunidades.html")


def buscar_empleo(request):
    if request.method == 'POST':  # Verificar si es un formulario POST
        puesto_palabra_clave = request.POST.get('puesto_palabra_clave', '').strip()  # Capturar "Puesto o palabra clave"
        ubicacion = request.POST.get('ubicacion', '').strip()

        # Verificar si hay datos y guardarlos
        if puesto_palabra_clave or ubicacion:
            BusquedaTrabajo.objects.create(
                palabra_clave=puesto_palabra_clave,  # Guardar "Puesto o palabra clave"
                ubicacion=ubicacion
            )
            print(f"Se guardó correctamente: Puesto o palabra clave - {puesto_palabra_clave}, Ubicación - {ubicacion}")
        else:
            print("No se guardó porque no se ingresaron datos.")

    # Obtener las búsquedas recientes
    busquedas = BusquedaTrabajo.objects.all().order_by('-fecha_busqueda')[:10]
    print(f"Búsquedas recientes: {busquedas}")

    return render(request, 'jobConet_app/buscarEmpleo.html', {'busquedas': busquedas})

def editar_perfil(request):
    return render(request, 'jobConet_app/editar_perfil.html')