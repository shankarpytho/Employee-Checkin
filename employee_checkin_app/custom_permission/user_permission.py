from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        print('----------request.user.admin',request.user)
        return request.user.role == 'admin'

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        print('----------request.user.role',request.user)
        return request.user.role == 'employee'
