from django.views import View
from rest_framework import permissions
from rest_framework.request import Request


class IsOwnerOrIsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or superusers to access it.
    """

    def has_object_permission(self, request: Request, view: View, obj: any) -> bool:
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return obj.user == request.user or request.user.is_superuser
