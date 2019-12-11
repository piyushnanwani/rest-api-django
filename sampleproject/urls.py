from django.contrib import admin
from django.urls import path
from users.user_api import UserViewSet
from rest_framework import routers
from django.conf.urls import url, include
from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
