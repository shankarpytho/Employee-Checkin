# myapp/serializers.py

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
from rest_framework import serializers
User = get_user_model()

class SuperUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            # email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.is_superuser = True  # Set the user as superuser
        user.is_staff = True  # Required for admin access
        user.role='admin'
        user.save()
        group, created = Group.objects.get_or_create(name="Admin")  # Create the group if it doesn't exist
        user.groups.add(group)
        return user

class EmployeeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            # email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.role='employee'
        user.is_superuser = False  # Not a superuser
        user.is_staff = False  # Not a staff user
        user.save()
        
        group, created = Group.objects.get_or_create(name="Employee")  # Create the group if it doesn't exist
        user.groups.add(group)  
        return user
