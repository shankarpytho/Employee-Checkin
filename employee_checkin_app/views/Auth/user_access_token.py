from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from  employee_checkin_app.serializers.custom_access_refresh.user_access_refresh_token import CustomTokenSerializer
class CustomTokenObtainView(APIView):
    permission_classes = [AllowAny]
    # serializer_class = CustomTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = CustomTokenSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            token_data = serializer.create(serializer.validated_data)
            return Response(token_data, status=status.HTTP_200_OK)  # 200 OK for successful login
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)  # 401 Unauthorized