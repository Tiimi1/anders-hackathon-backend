from rest_framework.viewsets import ModelViewSet

from notes.api.serializers import LocationModelSerializer, TaskModelSerializer
from notes.models import Location, Task


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationModelSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
