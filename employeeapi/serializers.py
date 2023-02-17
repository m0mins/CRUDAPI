from rest_framework import serializers
from . models import Employee
from rest_framework.validators import UniqueValidator


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('fullname','emp_code','mobile','image')
        extra_kwargs = {
                'mobile': {
                    'validators': [
                        UniqueValidator(
                            queryset=Employee.objects.all()
                        )
                    ]
                }
            }           