from rest_framework.permissions import BasePermission
from group.models import Member


class IsGroupAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        group_id = view.kwargs.get('pk')
        if group_id:
            return Member.objects.filter(group_id=group_id, user__user=request.user, is_admin=True).exists()
        return False
    