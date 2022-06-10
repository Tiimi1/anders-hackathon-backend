# Generated by Django 4.0.5 on 2022-06-10 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="group",
            name="creator",
        ),
        migrations.RemoveField(
            model_name="group",
            name="members",
        ),
        migrations.RemoveField(
            model_name="locationgroup",
            name="locations",
        ),
        migrations.RemoveField(
            model_name="task",
            name="assigned_group",
        ),
        migrations.RemoveField(
            model_name="task",
            name="category",
        ),
        migrations.RemoveField(
            model_name="task",
            name="creator",
        ),
        migrations.RemoveField(
            model_name="task",
            name="location_group",
        ),
        migrations.RemoveField(
            model_name="task",
            name="range",
        ),
        migrations.AddField(
            model_name="location",
            name="radius_meters",
            field=models.DecimalField(decimal_places=10, default=50, max_digits=13, verbose_name="Radius Meters"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="is_complete",
            field=models.BooleanField(default=False, verbose_name="Is Complete"),
        ),
        migrations.AddField(
            model_name="task",
            name="location",
            field=models.ForeignKey(
                default=None, on_delete=django.db.models.deletion.CASCADE, related_name="tasks", to="notes.location"
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.DeleteModel(
            name="Group",
        ),
        migrations.DeleteModel(
            name="LocationGroup",
        ),
    ]
