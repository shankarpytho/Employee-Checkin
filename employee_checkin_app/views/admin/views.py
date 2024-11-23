from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from  employee_checkin_app.models import CheckinDetails
from  employee_checkin_app.serializers.get_check_in import CheckOutDetailsSerializer
from employee_checkin_app.custom_permission.user_permission import IsAdmin
from rest_framework import status

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    def get(self,request):
        get_emp_checkins = CheckinDetails.objects.all()
        get_all_emp = CheckOutDetailsSerializer(get_emp_checkins, many=True)
        return Response(get_all_emp.data, status=status.HTTP_200_OK)
