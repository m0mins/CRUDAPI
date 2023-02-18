from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


class EmployeeViewset(viewsets.ModelViewSet):
    
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):           
            return Response(serializer.errors, status=400)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response({"Success": "New Employee Added"}, status=status.HTTP_201_CREATED, headers=headers)
