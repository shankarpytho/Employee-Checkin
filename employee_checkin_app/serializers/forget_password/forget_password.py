# serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str,force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from urllib.parse import quote
User = get_user_model()
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        # Check if user exists
        try:
            user = User.objects.get(email=value)
            print("--------------------user",user)
        except User.DoesNotExist:
            raise serializers.ValidationError("No account found with this email.")
        return value

    def send_reset_email(self, user):
        token = default_token_generator.make_token(user)
        print("=--------------token",token)
        uid = urlsafe_base64_encode(force_bytes(user.pk))  
        print("=--------------uid",uid)
        # decoded_string = uid.decode('utf-8', errors='ignore')
        # # URL encode the string
        # encoded_string = uid.decode('utf-8', errors='replace')
        # print("----------------uid",encoded_string)
        reset_url = f"http://127.0.0.1:8000/reset-password/{uid}/{token}/"
        # Send email
        send_mail(
            "Password Reset Request",
            f"Click the following link to reset your password: {reset_url}",
            settings.EMAIL_HOST_USER,
            [user.email],
        )

