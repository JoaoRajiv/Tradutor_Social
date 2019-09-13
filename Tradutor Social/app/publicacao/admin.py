from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from .models import Profile

admin.site.register(Profile, UserAdmin)
admin.site.register(models.Publication)
admin.site.register(models.Evaluation)
admin.site.register(models.Correction)

