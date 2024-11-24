from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from django.conf import settings

user = get_user_model()
class CustomTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        return user

    def create(self, validated_data):   
        user = validated_data
        refresh = RefreshToken.for_user(user)
        access_expiration =  settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
        refresh_expiration = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']
        return {
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role':user.role
            },
            "user_token":{
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'access_expires': int(access_expiration.total_seconds()),  # Return expiration in ISO 8601 format
                'refresh_expires': int(refresh_expiration.total_seconds()),

            }


        }