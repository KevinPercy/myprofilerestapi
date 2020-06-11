from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnPost(permissions.BasePermission):
    """Allow users to edit their own post"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class IsSuperuserOrIsSelf(permissions.BasePermission):
    """ Check if a user is logged in as superuser or is the self user"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to changes its own password"""
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return obj.id == request.user.id
