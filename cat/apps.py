from django.apps import AppConfig


class catConfig(AppConfig):
    name = 'cat'
    verbose_name = "Gestion des chats"

default_app_config = 'cat.apps.catConfig'