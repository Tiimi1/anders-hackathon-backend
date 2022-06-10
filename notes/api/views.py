from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from notes.api.serializers import LocationModelSerializer, TaskModelSerializer
from notes.models import Location, Task


class LocationViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Location.objects.all()
    serializer_class = LocationModelSerializer


class TaskViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
