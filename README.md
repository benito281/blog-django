# Proyecto desarrollado en python

## Descripción

Comprende un blog orientado a noticias y artículos

## Estructura del proyecto

```

├── blog-repo/					<--- Carpeta del Repositorio
│ ├── blog/					    <--- Carpeta del proyecto Django
│ │ ├── apps/					<--- Aplicaciones Django
│ │ │ ├── noticias/
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── migrations/		    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ ├── usuarios/
│ │ │ │ ├── __pycache__/        **Ignorada en el .gitignore**
│ │ │ │ ├── templatetags/
│ │ │ │ │ ├── __init__.py
│ │ │ │ │ └── custom_tags.py	 
│ │ │ │ ├── migrations/		    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ └── ...
│ │ ├── blog/
│ │ │ ├── __pycache__/		    **Ignorada en el .gitignore**
│ │ │ ├── configurations/	    <--- Configuraciones django (opcional)
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── local.py		    <--- Configuraciones para desarrollo local
│ │ │ │ ├── production.py	    <--- Configuraciones para produccion
│ │ │ │ ├── base.py		    <--- Configuraciones base
│ │ │ │ └── ...
│ │ │ ├── __init__.py
│ │ │ ├── asgi.py
│ │ │ ├── settings.py
│ │ │ ├── urls.py
│ │ │ ├── wsgi.py
│ │ │ └── ...
│ │ ├── media/				    <--- Archivos multimedia - **Podria ser ignorada en el .gitignore**
│ │ │ ├── noticias/
│ │ │ │ ├── ..Imagenes..
│ │ │ │ └── ...
│ │ │ ├── usuarios/
│ │ │ │ ├── ..Imagenes..
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── static/				    <--- Archivos estáticos
│ │ │ ├── img/
│ │ │ │ ├── ..Imagenes..
│ │ │ │ └── ...
│ │ │ ├── css/
│ │ │ │ ├── style.css
│ │ │ │ └── ...
│ │ │ ├── js/
│ │ │ │ ├── confirmar_eliminar.js
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── templates/			    <--- Archivos templates
│ │ │ ├── partials/
│ │ │ │ ├── footer.html
│ │ │ │ ├── navbar.html
│ │ │ │ └── ...
│ │ │ ├── base.html
│ │ │ ├── contacto.html
│ │ │ ├── home.html
│ │ │ ├── info.html
│ │ │ └── ...
│ │ │ ├── noticias/
│ │ │ │ ├── cargar_noticia.html
│ │ │ │ ├── detale_noticia.html
│ │ │ │ ├── home_noticias.html
│ │ │ │ ├── modificar_noticia.html
│ │ │ │ └── ...
│ │ │ ├── usuarios/
| │ │ │ ├── registration/
| | │ │ │ ├── password_reset_done.html
│ │ │ │ | └── ...
│ │ │ | ├── login.html
│ │ │ | └── ...
│ │ │ └── ...
│ │ ├── db.sqlite3			    <--- Base de datos - **Ignorada en el .gitignore**
│ │ ├── manage.py
│ │ └── ...
│ ├── entorno/						<--- Carpeta del entorno - **Ignorada en el .gitignore** 
│ │ ├── Scripts/
│ │ │ ├── activate.bat
│ │ │ ├── deactivate.bat
│ │ │ └── ...
│ │ └── ...
│ ├── .gitignore
│ ├── README.md				    <--- Archivo README.md - Describe el proyecto
│ ├── requeriments.txt		    <--- Archivo requeriments.txt - Enlista los paquetes
| └── ...
└── ...

```
## Usuarios
```
Super Usuario
nombre: superuser
Email: superuser@email.com
contraseña: facil123

Colaborador
nombre: colaborador
Email: colaborador@email.com
contraseña: facil123

Usuario Normal
nombre: usuario
Email: usuario@email.com
contraseña: facil123

```# blog-django
