from django.urls import path

from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register('boss', viewsets.BossViewSet)
router.register('user-boss', viewsets.UserBossViewSet)
router.register('user', viewsets.UserViewSet)
