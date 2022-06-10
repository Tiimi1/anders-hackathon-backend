from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from .api import LocationViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'tasks', TaskViewSet)
