from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
# from django.utils.encoding import force_str
# from django.utils.http import urlsafe_base64_decode  # Ensure this is imported

class ResetPasswordSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate(self, attrs):
        try:
            # # Decode the base64-encoded UID using urlsafe_base64_decode and convert it to string
            # uid = force_str(urlsafe_base64_decode(attrs['uid']))  # Decode the user ID from base64
            user = get_user_model().objects.get(pk=attrs['uid'])
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            raise serializers.ValidationError("Invalid user or token.")

        # Check if the token is valid for this user
        if not default_token_generator.check_token(user, attrs['token']):
            raise serializers.ValidationError("Invalid token.")

        attrs['user'] = user  # Add the user object to the validated data
        return attrs
