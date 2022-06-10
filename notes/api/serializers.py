from rest_framework.serializers import ModelSerializer

from notes.models import Location, Task


class LocationModelSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "longitude", "latitude", "name", "radius_meters")


class TaskModelSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "due_date",
            "location",
            "is_complete",
        )
