from django.apps import AppConfig

# Config a different settings for the app.
class ComputerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'computer_science_learning_app'
