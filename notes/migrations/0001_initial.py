# Generated by Django 4.0.5 on 2022-06-10 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("longitude", models.DecimalField(decimal_places=10, max_digits=10, verbose_name="Longitude")),
                ("Latitude", models.DecimalField(decimal_places=10, max_digits=10, verbose_name="Latitude")),
                ("name", models.CharField(max_length=63, verbose_name="Name")),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=63, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                ("due_date", models.DateTimeField(blank=True, null=True, verbose_name="Due date/time")),
                ("assigned_group", models.ManyToManyField(to="auth.group")),
                (
                    "creator",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
                ("location", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="notes.location")),
            ],
        ),
    ]
