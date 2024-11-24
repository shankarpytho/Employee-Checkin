from django.contrib import admin
from employee_checkin_app.models import CustomUser,CheckinDetails
# Register your models here.
admin.site.register(CustomUser)
# admin.site.register(Role)
admin.site.register(CheckinDetails)
