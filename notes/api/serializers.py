from rest_framework.serializers import ModelSerializer

from notes.models import Category, Group, Location, LocationGroup, Task


class LocationModelSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ("longitude", "latitude", "name")


class LocationGroupModelSerializer(ModelSerializer):
    class Meta:
        model = LocationGroup
        fields = ("locations", "name")


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "range")


class TaskModelSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "due_date",
            "location_group",
            "creator",
            "assigned_group",
            "range",
            "category",
        )


class GroupModelSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", "creator", "members")
