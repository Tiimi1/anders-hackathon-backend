from django.contrib import admin

from .models import Location, Task

admin.register(Location, Task)
