from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Location(models.Model):
    longitude = models.DecimalField(verbose_name=("Longitude"), max_digits=13, decimal_places=10)
    latitude = models.DecimalField(verbose_name=("Latitude"), max_digits=13, decimal_places=10)
    name = models.CharField(verbose_name=("Name"), max_length=63)


class LocationGroup(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=63)
    locations = models.ManyToManyField(Location)


class Category(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=63)
    range = models.PositiveSmallIntegerField(verbose_name=("Range"), blank=True, null=True)


class Group(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=63)
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="note_group")
    members = models.ManyToManyField(UserModel)


class Task(models.Model):
    title = models.CharField(verbose_name=("Name"), max_length=63)
    description = models.TextField(verbose_name=("Description"))
    range = models.PositiveSmallIntegerField(verbose_name=("Range"), blank=True, null=True)
    due_date = models.DateTimeField(verbose_name=("Due date/time"), blank=True, null=True)
    location_group = models.ForeignKey(LocationGroup, on_delete=models.CASCADE, related_name="tasks")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks")
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="tasks")
    assigned_group = models.ManyToManyField(Group)
