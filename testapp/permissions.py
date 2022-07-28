from rest_framework.permissions import BasePermission,SAFE_METHODS
class IsReadOnly(BasePermission):
    def has_permission(self,request,view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class Isgetorpatch(BasePermission):
    def has_permission(self,request,view):
        allowed_methods=['GET','PATCH']
        if request.method in allowed_methods:
            return True
        else:
            return False
        
class sunnypermissions(BasePermission):
    def has_permission(self,request,view):
        username=request.user.username
        if username.lower()=='sunny':
            return True
        elif len(username) != '' and len(username) %2 ==0 and request.method in SAFE_METHODS:
            return True
        else:
            return False