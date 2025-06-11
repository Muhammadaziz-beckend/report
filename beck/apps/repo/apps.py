from django.apps import AppConfig


class RepoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.repo"

    def ready(self):

        from . import signals
