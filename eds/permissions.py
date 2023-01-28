from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsSelectionOwner(BasePermission):
    message = "Вы не имеете права к подборке"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user: #.owner
            return True
        return False


class IsAdOwnerOrStaff(BasePermission):
    message = "Вы не имеете доступа"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author_id or request.user.role in [UserRoles.ADMIN, UserRoles.MODERATOR]:
            return True
        return False
