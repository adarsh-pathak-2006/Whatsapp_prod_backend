from rest_framework.permissions import BasePermission
from group.models import Member


class IsGroupAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and Member.is_admin==True
    