from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        is_safe_method = request.method in SAFE_METHODS
        is_authenticated = request.user.is_authenticated
        if not is_safe_method and not is_authenticated:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
