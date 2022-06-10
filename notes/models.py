from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


UserModel = get_user_model()


class Location(models.Model):
    longitude = models.DecimalField(verbose_name=("Longitude"), max_digits=13, decimal_places=10)
    latitude = models.DecimalField(verbose_name=("Latitude"), max_digits=13, decimal_places=10)
    name = models.CharField(verbose_name=("Name"), max_length=63)


class Task(models.Model):
    title = models.CharField(verbose_name=("Name"), max_length=63)
    description = models.TextField(verbose_name=("Description"))
    due_date = models.DateTimeField(verbose_name=("Due date/time"), blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    assigned_group = models.ManyToManyField(Group)
