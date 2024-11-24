from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from employee_checkin_app.custom_permission.user_permission import IsEmployee
from rest_framework import status
from employee_checkin_app.models import  CustomUser
from  employee_checkin_app.models import CheckinDetails
from  employee_checkin_app.serializers.get_check_in import CheckinDetailsSerializer,CheckOutDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication

class EmployeeOnlyView(APIView):

    permission_classes = [IsAuthenticated, IsEmployee]
    def get(self, request, employee_id):
        jwt_auth = JWTAuthentication()
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'error': 'Authorization header missing or invalid.'}, status=status.HTTP_401_UNAUTHORIZED)
        token = auth_header.split(' ')[1]
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
        get_user_name = CustomUser.objects.get(id =employee_id ).username
        # Filter checkins for the specified employee
        checkins = CheckinDetails.objects.filter(
            employee=employee_id
        )
        if user.id == user_id:
            serializer = CheckOutDetailsSerializer(checkins, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Token is not valid for this user.'}, status=status.HTTP_403_FORBIDDEN)

        
class CheckinDetailsCreateAPIView(APIView):
    try:
        permission_classes = [IsAuthenticated, IsEmployee]
        def post(self, request, *args, **kwargs):
            jwt_auth = JWTAuthentication()
            employee_id = request.data.get('employee')
            auth_header = request.META.get('HTTP_AUTHORIZATION')
            if not auth_header or not auth_header.startswith('Bearer '):
                return Response({'error': 'Authorization header missing or invalid.'}, status=status.HTTP_401_UNAUTHORIZED)
            token = auth_header.split(' ')[1]
            validated_token = jwt_auth.get_validated_token(token)
            user = jwt_auth.get_user(validated_token)
            get_user_name = CustomUser.objects.get(id =employee_id ).id
            if user.id == get_user_name:
                serializer = CheckinDetailsSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Token is not valid for this user.'}, status=status.HTTP_403_FORBIDDEN)


    except Exception as e:
        print(traceback.format_exc())
class CheckOutDetailsCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsEmployee]
    
    def put(self, request):
        
        jwt_auth = JWTAuthentication()
        employee_id = request.data.get('employee')
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'error': 'Authorization header missing or invalid.'}, status=status.HTTP_401_UNAUTHORIZED)
        token = auth_header.split(' ')[1]
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
        
        
        
        if user.id == employee_id:
            checkin_id = request.data.get('checkin_id')
            serializer = CheckOutDetailsSerializer(data=request.data)
            checkin = get_object_or_404(CheckinDetails, checkin_id=checkin_id)
            # Update the checkout_time from the request data
            checkout_time = request.data.get("checkout_time")
            modified_by =  request.data.get("modified_by")
            created_by =  request.data.get("created_by")
            location =  request.data.get("location")
            employee_name =  request.data.get("employee_name")
            checkin.checkout_time = checkout_time
            checkin.modified_by = modified_by
            checkin.created_by = created_by
            checkin.location = location
            checkin.employee_name = employee_name
            checkin.save()

            # Serialize the updated record
            serializer = CheckOutDetailsSerializer(checkin)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Token is not valid for this user.'}, status=status.HTTP_403_FORBIDDEN)
