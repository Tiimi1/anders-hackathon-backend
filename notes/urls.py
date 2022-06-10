from rest_framework import routers

from notes.api.views import CategoryViewSet, GroupViewSet, LocationGroupViewSet, LocationViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r"locations", LocationViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"location-groups", LocationGroupViewSet)
router.register(r"groups", GroupViewSet)
