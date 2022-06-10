from rest_framework import routers

from notes.api.views import LocationViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r"locations", LocationViewSet)
router.register(r"tasks", TaskViewSet)
