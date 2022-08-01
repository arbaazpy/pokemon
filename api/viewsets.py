from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from .models import Boss, UserBoss
from rest_framework import viewsets
from .serializers import BossSerializer, UserBossSerializer, CreateUserSerializer


class BossViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Boss.objects.all()
    serializer_class = BossSerializer


class UserBossViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserBoss.objects.all()
    serializer_class = UserBossSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
