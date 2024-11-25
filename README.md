# JobConet

**JobConet** es una aplicación web desarrollada en Django que permite a los usuarios crear perfiles profesionales, conectarse con otros profesionales, buscar oportunidades laborales y compartir contenido profesional.

## **Características Principales**
1. **Registro de Usuarios**
   - Registro mediante correo electrónico con confirmación.
   - Registro usando redes sociales (Google, Facebook, LinkedIn).
2. **Autenticación y Seguridad**
   - Inicio de sesión seguro.
   - Autenticación de dos factores (2FA).
   - Recuperación de contraseñas.
3. **Gestión de Perfiles**
   - Creación y edición de perfiles profesionales.
   - Configuración de privacidad para controlar la visibilidad del perfil.
4. **Conexiones Profesionales**
   - Envío y gestión de solicitudes de conexión.
   - Visualización y categorización de conexiones.
5. **Búsqueda y Publicación de Empleos**
   - Búsqueda avanzada de ofertas laborales.
   - Aplicación directa a ofertas desde la plataforma.
6. **Publicaciones y Contenido**
   - Creación de publicaciones (texto, imágenes, videos).
   - Estadísticas de interacciones en publicaciones.
7. **Notificaciones y Mensajería**
   - Sistema de notificaciones en tiempo real.
   - Mensajería directa entre usuarios.

---

## **Tecnologías Utilizadas**
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Base de Datos**: SQLite (desarrollo), PostgreSQL (producción)
- **Autenticación Social**: Django-Allauth
- **Correo Electrónico**: Gmail SMTP para confirmación y recuperación de contraseña

---

## **Instalación y Configuración**
### **Requisitos Previos**
- Python 3.8+
- Django 4.2+
- Entorno virtual (recomendado)

### **Pasos para Configuración**
1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/tu-usuario/jobconet.git
   cd jobconet
Crear y Activar el Entorno Virtual

bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Instalar Dependencias

bash
pip install -r requirements.txt
Configurar Variables de Entorno

Crear un archivo .env en la raíz del proyecto:
makefile
Copiar código
SECRET_KEY='tu-secreto'
DEBUG=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='tu-correo@gmail.com'
EMAIL_HOST_PASSWORD='tu-contraseña'
Realizar Migraciones

bash
python manage.py makemigrations
python manage.py migrate
Ejecutar el Servidor

bash
python manage.py runserver
Pruebas
Ejecuta las pruebas unitarias para asegurar el correcto funcionamiento:
bash
python manage.py test
Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request con mejoras o correcciones.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Contacto
Autor: 
Correo Electrónico: 
