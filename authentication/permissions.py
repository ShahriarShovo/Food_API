from rest_framework.permissions import BasePermission

class IsOwnerOrEmployee(BasePermission):
    """
    Custom permission to only allow owners or employees to create menus, items, categories, and modifiers.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role in ['owner', 'employee']
