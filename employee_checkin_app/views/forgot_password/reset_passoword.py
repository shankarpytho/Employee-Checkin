# views.py
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from employee_checkin_app.serializers.forget_password.reset_password import ResetPasswordSerializer
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode

class ResetPasswordSubmitView(APIView):
    def post(self, request,uid,token):
        secret = request.POST.getlist('password2')[0]
        serializer = ResetPasswordSerializer(data={"uid":uid,"token":token,"password":secret})
        if serializer.is_valid():
            try:
                user = get_user_model().objects.get(pk=uid)
                token = token
            except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
                return Response({"detail": "Invalid user or token."}, status=status.HTTP_400_BAD_REQUEST)

            if not default_token_generator.check_token(user, token):
                return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)

            # Set the new password and save the user
            user.set_password(serializer.validated_data['password'])
            user.save()
            return render(request,'reset_passoword_msg.html',{'reset_status': "success", "message": "Password reset successfully."})
            # return Response({"message": "Password reset successfully."}, status=status.HTTP_200_OK)

        return render(request,'reset_passoword_msg.html',{'reset_status': "failure", "message":serializer.errors})
        # Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
