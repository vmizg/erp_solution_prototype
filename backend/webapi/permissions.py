from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of their Employee profile to edit it
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the employee
        return obj.user == request.user


class IsAdminOrDeny(permissions.BasePermission):
    """
    Custom permission to only allow admins to view EmployeeContracts.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsOwnerOrDeny(permissions.BasePermission):
    """
    Custom permission to only allow owners of an EmployeeContract to edit it,
    otherwise deny access completely.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request from admin
        if request.method in permissions.SAFE_METHODS and request.user.is_superuser:
            return True

        # Write permissions are only allowed to the contract employee
        return obj.user == request.user