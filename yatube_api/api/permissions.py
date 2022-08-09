from rest_framework import permissions


class AuthorAccess(permissions.BasePermission):

    def have_access(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
