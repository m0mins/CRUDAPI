# Generated by Django 3.2.17 on 2023-02-16 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0004_employee_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
    ]
