from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from employee_checkin_app.custom_permission.user_permission import IsEmployee
from rest_framework import status
from  employee_checkin_app.models import CheckinDetails
from  employee_checkin_app.serializers.get_check_in import CheckinDetailsSerializer,CheckOutDetailsSerializer
from django.shortcuts import get_object_or_404

class EmployeeOnlyView(APIView):

    permission_classes = [IsAuthenticated, IsEmployee]
    def get(self, request, employee_id):
        # print(employee_id)
        # Filter checkins for the specified employee
        checkins = CheckinDetails.objects.filter(
            employee=employee_id
        )
        print(checkins)
        serializer = CheckOutDetailsSerializer(checkins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class CheckinDetailsCreateAPIView(APIView):
    try:
        permission_classes = [IsAuthenticated, IsEmployee]
        def post(self, request, *args, **kwargs):
            serializer = CheckinDetailsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(traceback.format_exc())
class CheckOutDetailsCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsEmployee]
    def put(self, request):
        serializer = CheckOutDetailsSerializer(data=request.data)
        
        # if serializer.is_valid():
        #     serializer.save()
            
        checkin_id = request.data.get('checkin_id')
        print("------------checkin",checkin_id)
        checkin = get_object_or_404(CheckinDetails, checkin_id=checkin_id)
        print("------------checkouttttttt",checkin)

        # Update the checkout_time from the request data
        checkout_time = request.data.get("checkout_time")
        modified_by =  request.data.get("modified_by")
        created_by =  request.data.get("created_by")
        location =  request.data.get("location")
        employee_name =  request.data.get("employee_name")

            # if not checkout_time or modified_by or created_by or location  or employee_name:
            #     return Response({"error": "checkout_time is required."}, status=status.HTTP_400_BAD_REQUEST)

        checkin.checkout_time = checkout_time
        checkin.modified_by = modified_by
        checkin.created_by = created_by
        checkin.location = location
        checkin.employee_name = employee_name
        checkin.save()

        # Serialize the updated record
        serializer = CheckOutDetailsSerializer(checkin)
        return Response(serializer.data, status=status.HTTP_200_OK)
