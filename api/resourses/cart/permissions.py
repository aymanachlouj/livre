from rest_framework import permissions

class CartPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return False
