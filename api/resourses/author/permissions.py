from rest_framework import permissions

class AuthorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return False
