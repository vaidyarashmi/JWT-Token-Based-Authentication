from django.forms import ValidationError
from testapp.models import Employee
from rest_framework.serializers import ModelSerializer

class EmployeeSerializer(ModelSerializer):
    
    class Meta:
        model=Employee
        fields='__all__'
    def validate(self,data):
        esal=data.get('esal')
        if esal < 5000:
            raise ValidationError('Salary should be more than 5000')
        return data