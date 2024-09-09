"""
URL configuration for movio_auth_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny 


# service documentation
doc_schema_view = get_schema_view(
    openapi.Info(
        title="Movio Auth API",
        default_version="v1.0",
        description="API Endpoints for Movio Auth Service. Movio is a Video On Demand Platform Just Like YouTube",
        contact=openapi.Contact(email="iammahboob.a@gmail.com"),
        license=openapi.License(name="MIT Licence"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)


# Root Urls
urlpatterns = [
    # Admin
    path(settings.ADMIN_URL, admin.site.urls),
    # Doc
    path("doc/", doc_schema_view.with_ui("redoc", cache_timeout=0)),
    # Common: Healthcheck
    path("api/v1/common/", include("core_apps.common.urls")),
    
    # Auth APIs - User Registration, Login, Logout, etc.
    path("api/v1/auth/", include("core_apps.users.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Movio Auth Service API"
admin.site.site_title = "Movio Auth Service Admin Portal"
admin.site.index_title = "Welcome to Movio Auth Service API Portal"
