from django.contrib import admin
from todo_app import models

admin.site.register(models.Task)
admin.site.register(models.Category)
