from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
# custom permissions--------------->
from testapp.permissions import IsReadOnly,Isgetorpatch,sunnypermissions
# Create your views here.

class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[TokenAuthentication,]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly,]
    permission_classes=[sunnypermissions,]