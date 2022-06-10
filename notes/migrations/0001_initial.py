# Generated by Django 4.0.5 on 2022-06-10 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=63, verbose_name="Name")),
                ("range", models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Range")),
            ],
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=63, verbose_name="Name")),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="note_group",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("members", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("longitude", models.DecimalField(decimal_places=10, max_digits=13, verbose_name="Longitude")),
                ("latitude", models.DecimalField(decimal_places=10, max_digits=13, verbose_name="Latitude")),
                ("name", models.CharField(max_length=63, verbose_name="Name")),
            ],
        ),
        migrations.CreateModel(
            name="LocationGroup",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=63, verbose_name="Name")),
                ("locations", models.ManyToManyField(to="notes.location")),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=63, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                ("range", models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Range")),
                ("due_date", models.DateTimeField(blank=True, null=True, verbose_name="Due date/time")),
                ("assigned_group", models.ManyToManyField(to="notes.group")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="tasks", to="notes.category"
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="tasks", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "location_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="tasks", to="notes.locationgroup"
                    ),
                ),
            ],
        ),
    ]
