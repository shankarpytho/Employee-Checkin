# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode  
from employee_checkin_app.serializers.forget_password.reset_password import ResetPasswordSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from django.utils.encoding import force_str
class ResetPasswordPageView(APIView):
    def get(self, request, uid, token):
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            return JsonResponse({'detail': 'Invalid or expired token.'}, status=400)

        # Validate token
        if not default_token_generator.check_token(user, token):
            return JsonResponse({'detail': 'Invalid or expired token.'}, status=400)

        # If token is valid, render the reset password page
        return render(request, 'reset_password.html', {'uid': uid, 'token': token})
