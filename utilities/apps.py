from django.apps import AppConfig


class UtilitesConfig(AppConfig):
    name = 'utilites'
    def ready(self):
        from . import custom