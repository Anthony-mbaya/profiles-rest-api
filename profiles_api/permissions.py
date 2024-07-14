from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """"allow use edit own prof"""
    def has_object_permission(self, request, view, obj):
        """check if user is trying to edit hteir own profile"""
        if request.method in permissions.SAFE_METHODS:#check if method is safe = ONLY GET IS SAFE_METHODS
            return True
        return obj.id == request.user.id #return True is user is trying to update own profile and false for opposite
