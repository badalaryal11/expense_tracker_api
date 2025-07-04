from rest_framework import permissions

class IsOwnerOrIsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or an admin to see it.
    """
    def has_object_permission(self, request, view, obj):
        # Object-level permission to only allow owners or superusers.
        return obj.user == request.user or request.user.is_superuser

