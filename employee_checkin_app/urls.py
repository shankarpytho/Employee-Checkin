from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from employee_checkin_app.views.admin.views import AdminOnlyView
from employee_checkin_app.views.employee.views import CheckinDetailsCreateAPIView,EmployeeOnlyView,CheckOutDetailsCreateAPIView
from employee_checkin_app.views.Auth.user_access_token import CustomTokenObtainView
from employee_checkin_app.views.create_users.create_user import CreateEmployeeUserView,CreateSuperuserView
from django.urls import path,include

urlpatterns = [
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/', CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/admin/', AdminOnlyView.as_view(), name='admin_only'),
    path('api/checkins/<int:employee_id>/', EmployeeOnlyView.as_view(), name='employee-checkin-details'),
    path('api/checkin/', CheckinDetailsCreateAPIView.as_view(), name='create_checkin'),
    path('api/checkout/', CheckOutDetailsCreateAPIView.as_view(), name='create_checkout'),
    path('api/create-superuser/', CreateSuperuserView.as_view(), name='create-superuser'),
    path('api/create-employee/', CreateEmployeeUserView.as_view(), name='create-employee')

]
