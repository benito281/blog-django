from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.usuarios'

    #Se ejecutan los permisos para cada rol
    def ready(self):
        import apps.usuarios.signals