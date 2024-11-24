from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from  employee_checkin_app.models import CheckinDetails
from  employee_checkin_app.serializers.get_check_in import CheckOutDetailsSerializer
from employee_checkin_app.custom_permission.user_permission import IsAdmin
from rest_framework import status
from employee_checkin_app.models import  CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def post(self,request):
        admin_id = request.data.get('id')
        jwt_auth = JWTAuthentication()
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'error': 'Authorization header missing or invalid.'}, status=status.HTTP_401_UNAUTHORIZED)
        token = auth_header.split(' ')[1] 
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
        if user.id == admin_id:
            get_emp_checkins = CheckinDetails.objects.all()
            get_all_emp = CheckOutDetailsSerializer(get_emp_checkins, many=True)
            return Response(get_all_emp.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Token is not valid for this user.'}, status=status.HTTP_403_FORBIDDEN)
