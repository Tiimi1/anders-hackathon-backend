# Generated by Django 4.0.5 on 2022-06-10 14:24

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations
from django.contrib.postgres.operations import CreateExtension


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0003_category_range_task_range"),
    ]

    operations = [
        CreateExtension("postgis"),
        migrations.RemoveField(
            model_name="location",
            name="latitude",
        ),
        migrations.RemoveField(
            model_name="location",
            name="longitude",
        ),
        migrations.AddField(
            model_name="location",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(
                default=django.contrib.gis.geos.point.Point(1.0, 1.0), srid=4326, verbose_name="Location"
            ),
        ),
    ]