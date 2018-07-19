from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import *
from rest_framework import routers, serializers, viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),

]