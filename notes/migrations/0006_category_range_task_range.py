# Generated by Django 4.0.5 on 2022-06-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0005_remove_category_range_remove_location_location_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="range",
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Range"),
        ),
        migrations.AddField(
            model_name="task",
            name="range",
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Range"),
        ),
    ]