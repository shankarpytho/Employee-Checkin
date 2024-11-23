from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
import uuid

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')


class CheckinDetails(models.Model):
    # Use a string reference to avoid circular imports
    employee = models.ForeignKey('employee_checkin_app.CustomUser', on_delete=models.CASCADE, related_name="checkins")
    checkin_id = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
    employee_name = models.CharField(max_length=255,null=True, blank=True)
    # employee_id = models.CharField(max_length=50)
    checkin_time = models.DateTimeField(null=True, blank=True)
    checkout_time = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(default=now)
    location = models.CharField(max_length=255,null=True, blank=True)
    modified =  models.DateTimeField(default=now,null=True, blank=True)
    created_by = models.CharField(max_length=255,null=True, blank=True)
    modified_by = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.checkin_time}"

# class CheckOutDetails(models.Model):
#     # Use a string reference to avoid circular imports
#     employee = models.ForeignKey('employee_checkin_app.CustomUser', on_delete=models.CASCADE)
#     checkin_id = models.ForeignKey('employee_checkin_app.CheckinDetails', on_delete=models.CASCADE)
#     checkout_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     employee_name = models.CharField(max_length=255)
#     # employee_id = models.CharField(max_length=50)
#     checkout_time = models.DateTimeField()
#     # checkout_time = models.DateTimeField(null=True, blank=True)
#     created_date = models.DateTimeField(default=now)
#     location = models.CharField(max_length=255)
#     modified =  models.DateTimeField(default=now)

#     def __str__(self):
#         return f"{self.employee_name} - {self.checkout_time}"

