from django.apps import AppConfig


class UtilitesConfig(AppConfig):
    name = 'utilities'
    def ready(self):
        import custom