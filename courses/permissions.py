from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
  def has_permission(self, request, view):
      if request.method == 'DELETE' and not request.user.is_superuser:
          return False
      return True
