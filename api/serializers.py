from django.contrib.auth.models import User


from rest_framework import serializers

from .models import Boss, UserBoss


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class BossSerializer(serializers.ModelSerializer):
    def validate(self, data):
        data["name"]  = data["name"].title()
        if Boss.objects.filter(name=data["name"]).exists():
            raise serializers.ValidationError("Name already exists!")
        return data

    class Meta:
        model = Boss
        fields = "__all__"


class UserBossSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBoss
        fields = "__all__"