from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission): # to check if owner has permission to edit etc or not
    def has_object_permission(Self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #from the permissions library
            return True
        return obj.owner == request.user
