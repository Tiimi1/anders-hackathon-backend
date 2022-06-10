import decimal

from django.conf import settings
from django.db.models import Case, F, IntegerField, When
from django.db.models.functions import ATan2, Cast, Cos, Power, Radians, Sin, Sqrt
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

    def get_queryset(self):
        queryset = super().get_queryset()
        longitude = self.request.GET.get("longitude", None)
        latitude = self.request.GET.get("latitude", None)
        if longitude and latitude:
            queryset = queryset.annotate(
                task_range=Case(
                    When(range__isnull=False, then=F("range")),
                    When(category__range__isnull=False, then=F("category__range")),
                    default=Cast(settings.DEFAULT_NOTES_RANGE, IntegerField()),
                    output_field=IntegerField(),
                ),
            )

            dlat = Radians(F("latitude") - decimal.Decimal(latitude))
            dlong = Radians(F("longitude") - decimal.Decimal(longitude))

            a = Power(Sin(dlat / 2), 2) + Cos(Radians(decimal.Decimal(latitude))) * Cos(Radians(F("latitude"))) * Power(
                Sin(dlong / 2), 2
            )

            c = 2 * ATan2(Sqrt(a), Sqrt(1 - a))
            d = 6371 * c

            queryset = queryset.annotate(
                task_range=Case(
                    When(range__isnull=False, then=F("range")),
                    When(category__range__isnull=False, then=F("category__range")),
                    default=Cast(settings.DEFAULT_NOTES_RANGE, IntegerField()),
                    output_field=IntegerField(),
                ),
            )

            ids = set()

            for task in queryset:
                distances = task.location_group.locations.annotate(distance=d)
                if distances.filter(distance__lte=1).exists():
                    ids.add(task.id)
            return Task.objects.filter(id__in=ids)
        else:
            return queryset.none()


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
