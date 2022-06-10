from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Location(models.Model):
    longitude = models.DecimalField(verbose_name=("Longitude"), max_digits=28, decimal_places=18)
    latitude = models.DecimalField(verbose_name=("Latitude"), max_digits=28, decimal_places=18)
    name = models.CharField(verbose_name=("Name"), max_length=63)
    radius_meters = models.DecimalField(verbose_name=("Radius Meters"), max_digits=28, decimal_places=18)


class Task(models.Model):
    title = models.CharField(verbose_name=("Name"), max_length=63)
    description = models.TextField(verbose_name=("Description"))
    due_date = models.DateTimeField(verbose_name=("Due date/time"), blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="tasks")
    is_complete = models.BooleanField(verbose_name=("Is Complete"), default=False)
