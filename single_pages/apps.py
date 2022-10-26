from django.apps import AppConfig
from django.conf import settings

class SinglePagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "single_pages"

    def ready(self):
        from jobs import updater
        updater.start()