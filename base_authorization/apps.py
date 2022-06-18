from django.apps import AppConfig


class BaseAuthorizationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_authorization'
