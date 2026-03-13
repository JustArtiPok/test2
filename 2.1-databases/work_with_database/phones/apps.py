from django.apps import AppConfig

class PhonesConfig(AppConfig):  # имя должно быть уникальным
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phones'