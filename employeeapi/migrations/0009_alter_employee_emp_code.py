# Generated by Django 3.2.17 on 2023-02-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0008_alter_employee_emp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_code',
            field=models.CharField(max_length=10),
        ),
    ]