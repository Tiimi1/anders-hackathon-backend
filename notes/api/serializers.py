from rest_framework.serializers import HyperlinkedModelSerializer

from notes.models import Category, Group, Location, LocationGroup, Task


class LocationModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ("longitude", "latitude", "name")


class LocationGroupModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = LocationGroup
        fields = ("locations", "name")


class CategoryModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "name"


class TaskModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ("title", "description", "due_date", "location", "creator", "assigned_group")


class GroupModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("name", "creator", "members")
