from django.apps import AppConfig


class BaseAbstractsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DjangoBase.base_abstracts'
