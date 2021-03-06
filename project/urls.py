from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from notes.urls import router

schema_view = get_schema_view(
    openapi.Info(
        title="Locotodo API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    path("api/", include(router.urls)),
]
