from rest_framework.serializers import ModelSerializer

from notes.models import Category, Group, Location, LocationGroup, Task


class LocationModelSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "longitude", "latitude", "name")


class LocationGroupModelSerializer(ModelSerializer):
    locations = LocationModelSerializer(many=True)

    class Meta:
        model = LocationGroup
        fields = ("id", "locations", "name")


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "range")


class TaskModelSerializer(ModelSerializer):
    location_group = LocationGroupModelSerializer()

    class Meta:
        model = Task
        fields = (
            "id",
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
        fields = ("id", "name", "creator", "members")
