from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Location, Task


class LocationModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('longitude', 'latitude', 'name')


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationModelSerializer


class TaskModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date', 'location', 'creator', 'assigned_group')


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
