"""
URL configuration for MTest project.

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
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from user.views import CarListingViewSet, car_listing_search
from user.views import (
    UserViewSet,
    UserLogIn,
    LogoutView,
    ContactViewSet,
    ProductViewSet,
)
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
# router.register(r'car-list', CarListingViewSet)
router.register(r"users", UserViewSet)
router.register(r"lead-generation", ContactViewSet)
router.register(r"profile", ProductViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Test2 API",
        default_version="v1",
        description="Test2 apis for products",
    ),
    public=True,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api-user-login/", UserLogIn.as_view()),
    path("api-user-logout/", LogoutView.as_view()),
    # path('', car_listing_search, name='car_listing_search'),
    path("api-token-auth/", obtain_auth_token, name="obtain_auth_token"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
