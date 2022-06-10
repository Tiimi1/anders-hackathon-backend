from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from notes.api.serializers import (
    CategoryModelSerializer,
    GroupModelSerializer,
    LocationGroupModelSerializer,
    LocationModelSerializer,
    TaskModelSerializer,
)
from notes.models import Category, Group, Location, LocationGroup, Task


class LocationViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Location.objects.all()
    serializer_class = LocationModelSerializer


class TaskViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class CategoryViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class LocationGroupViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = LocationGroup.objects.all()
    serializer_class = LocationGroupModelSerializer


class GroupViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
