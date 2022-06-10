# Generated by Django 4.0.5 on 2022-06-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0002_rename_latitude_location_latitude"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="latitude",
            field=models.DecimalField(decimal_places=10, max_digits=13, verbose_name="Latitude"),
        ),
        migrations.AlterField(
            model_name="location",
            name="longitude",
            field=models.DecimalField(decimal_places=10, max_digits=13, verbose_name="Longitude"),
        ),
    ]
