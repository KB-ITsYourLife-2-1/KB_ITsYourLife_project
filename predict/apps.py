from django.apps import AppConfig
from django.conf import settings

class PredictConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "predict"

    def ready(self):
        #print("preditc_apps_ready()_function")
        from jobs import updater
        updater.start()