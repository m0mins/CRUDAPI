from django.db import models

def nameFile(instance, filename):
     return '/'.join(['images', filename])
    # return '/'.join(['images', str(instance.name), filename])

class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=10)
    # emp_code=models.SlugField(max_length=255)
    mobile=models.CharField(max_length=15)
    random_number=models.SlugField(max_length=255)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)   
    
