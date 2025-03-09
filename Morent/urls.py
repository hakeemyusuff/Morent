"""
URL configuration for Morent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("morent/v1/", include("car_rental.urls")),
    path("morent/v1/auth/", include("djoser.urls")),
    path("morent/v1/auth/", include("djoser.urls.jwt")),
    # path(
    #     "morent/v1/auth/token/",
    #     TokenObtainPairView.as_view(),
    #     name="token_obtain_pair",
    # ),
    # path(
    #     "morent/v1/auth/token/refresh/",
    #     TokenRefreshView.as_view(),
    #     name="token_refresh",
    # ),
]

urlpatterns += [
    path("morent/v1/auth/jwt/blacklist", TokenBlacklistView.as_view(), name="token_blacklist")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
