from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsEmployeeOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_employee:
            return True
        return request.method in SAFE_METHODS

class IsClientOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.client:
            return True
        return request.method in SAFE_METHODS
