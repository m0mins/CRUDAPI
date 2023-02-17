from rest_framework import serializers
from . models import Employee
from rest_framework.validators import UniqueValidator
from coolname import generate_slug


class EmployeeSerializer(serializers.ModelSerializer):
    random_number = serializers.CharField(
        min_length=3, 
        max_length=25, 
        validators=[UniqueValidator(queryset=Employee.objects.all())], 
        allow_null=True, 
        default=None
    )
    class Meta:
        model=Employee
        fields=('fullname','emp_code','mobile','random_number','image')
        extra_kwargs = {
                'mobile': {
                    'validators': [
                        UniqueValidator(
                            queryset=Employee.objects.all()
                        )
                    ]
                }
            }
    def validate_random_number(self, val):
        return val or generate_slug()           