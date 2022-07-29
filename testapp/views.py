from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
#jwt authentication---------------->
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# custom jwt authentication
from testapp.authentication import CustomAuthentication,CustomAuthentication2
#token based authentication---------->
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
# custom permissions--------------->
from testapp.permissions import IsReadOnly,Isgetorpatch,sunnypermissions
# Create your views here.

class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[CustomAuthentication2,]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly,]
    permission_classes=[IsAuthenticated,]