from rest_framework import serializers
from employee_checkin_app.models import CheckinDetails
from employee_checkin_app.models import CustomUser
class EmployeeSerializer(serializers.ModelSerializer):
    # Serialize employee details
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email','role']
class CheckinDetailsSerializer(serializers.ModelSerializer):
    # employee = EmployeeSerializer()
    class Meta:
        
        model = CheckinDetails
        fields = ['employee',"employee_name","checkin_time","location","modified_by","checkin_id"]  # Include all fields or specify particular ones
        

class CheckOutDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckinDetails
        fields = ['employee',"checkin_id","employee_name","checkin_time","checkout_time","created_date","modified","location","created_by","modified_by"]  # Include all fields or specify particular ones
