from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def user_has_permission(self, request, view, obj):
        # for now any user can view any object : GET, HEAD or OPTIONS
        #permission neeeded to edit
        if request.method in permissions.SAFE_METHODS:
            return True

        # edit is allowed to the owner of the object.
        return obj.owner == request.user