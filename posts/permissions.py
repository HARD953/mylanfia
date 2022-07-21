from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


# from rest_framework.permissions import BasePermission
 
# class IsAdminAuthenticated(BasePermission):
 
#     def has_permission(self, request, view):
#     # Ne donnons l’accès qu’aux utilisateurs administrateurs authentifiés
#         return bool(request.user and request.user.is_authenticated and request.user.is_superuser)