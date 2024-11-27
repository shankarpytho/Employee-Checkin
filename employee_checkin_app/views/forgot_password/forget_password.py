from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from employee_checkin_app.serializers.forget_password.forget_password import ForgotPasswordSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
class ForgotPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=serializer.validated_data['email'])
            serializer.send_reset_email(user)
            return Response({"message": "Password reset email sent."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)