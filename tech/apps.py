from django.apps import AppConfig
from typing import Any


class TechConfig(AppConfig):
    default_auto_field: Any = 'django.db.models.BigAutoField'
    name: str = 'tech'