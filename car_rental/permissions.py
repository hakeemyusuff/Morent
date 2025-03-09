from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminorReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.role == "admin"
    
    
class IsReviewOwnerorAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if obj.user == request.user:
            return True
        
        return request.user.role == "admin" and request.method == "DELETE"
        # if request.user.bookings
        
        
class BookingPermission(BasePermission):
    def has_permission(self, request, view):
            return request.user.is_authenticated
        
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        
        if request.method in SAFE_METHODS:
            return True