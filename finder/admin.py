from django.contrib import admin

from . import models

# Registering models to the admin site
admin.site.register(models.Target)
admin.site.register(models.Definition)
admin.site.register(models.Finding)