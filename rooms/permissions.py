from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    message = 'You are not a superuser.'

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
