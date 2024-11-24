from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from employee_checkin_app.custom_permission.user_permission import IsAdmin
from rest_framework import status
from  employee_checkin_app.serializers.role_assignment_serializer import EmployeeUserSerializer,SuperUserSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication


class CreateSuperuserView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def post(self, request):
        jwt_auth = JWTAuthentication()
        _admin = request.data.get('admin_id')
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'error': 'Authorization header missing or invalid.'}, status=status.HTTP_401_UNAUTHORIZED)
        token = auth_header.split(' ')[1]
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
        if user.id == _admin:
            serializer = SuperUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:

            return Response({'error': 'Token is not valid for this user.'}, status=status.HTTP_403_FORBIDDEN)


class CreateEmployeeUserView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def post(self, request):
        jwt_auth = JWTAuthentication()
        _admin = request.data.get('admin_id')
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'error': 'Authorization header missing or invalid.'}, status=status.HTTP_401_UNAUTHORIZED)
        token = auth_header.split(' ')[1]
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
        print("---------------u_adminser",_admin)
        serializer = EmployeeUserSerializer(data=request.data)
        if user.id == _admin:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Token is not valid for this user.'}, status=status.HTTP_403_FORBIDDEN)