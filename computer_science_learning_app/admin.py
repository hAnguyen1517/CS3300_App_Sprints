# Import the admin module from Django
from django.contrib import admin

# Import the models that need to be registered

from .models import Usersys, Game, LearningResource, Progress, PerformanceReport

# Register each model with the admin site
admin.site.register(Usersys)  # Register the User model
admin.site.register(Game)  # Register the Game model
admin.site.register(LearningResource)  # Register the LearningResource model
admin.site.register(Progress)  # Register the Progress model
admin.site.register(PerformanceReport)  # Register the PerformanceReport model
