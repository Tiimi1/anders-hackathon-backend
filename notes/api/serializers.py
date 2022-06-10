from rest_framework.serializers import HyperlinkedModelSerializer

from notes.models import Location, Task


class LocationModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ("longitude", "latitude", "name")


class TaskModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ("title", "description", "due_date", "location", "creator", "assigned_group")
