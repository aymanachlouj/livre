from rest_framework import permissions

class BookPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return False
