from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ride

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class RideSerializer(serializers.ModelSerializer):
    rider_username = serializers.CharField(source='rider.username', read_only=True)
    driver_username = serializers.CharField(source='driver.user.username', read_only=True)

    class Meta:
        model = Ride
        fields = '__all__'
