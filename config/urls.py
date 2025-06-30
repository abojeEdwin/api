from django.conf import settings
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView,)


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]
