from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import viewsets, renderers
from.views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'men', MenViewSet)
router.register(r'women', WomenViewSet)
router.register(r'All_data', MainViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)