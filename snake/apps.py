from django.apps import AppConfig


class snakeConfig(AppConfig):
    name = 'snake'
    verbose_name = "Gestion des serpents"

default_app_config = 'snake.apps.snakeConfig'