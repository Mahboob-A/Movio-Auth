from django.urls import path

from core_apps.common.views import HealthCheck

urlpatterns = [
    path("healthcheck/", HealthCheck.as_view(), name="healthcheck"),
]
