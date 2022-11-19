from email.policy import default
from django.db import models

# Create your models here.
class Emp(models.Model):
    # name = models.CharField(max_length=200)
    # # emp_id = models.IntegerField( blank=True , null=True )
    # # phone = models.IntegerField( blank=True , null=True )
    # address = models.CharField(max_length=200)
    # working = models.BooleanField()
    # department = models.CharField(max_length=200)
    name = models.CharField(max_length=200, default='Mujahid')
    employee_id = models.IntegerField(default=0)
    phone_no = models.IntegerField(default=9507008142)
    address = models.CharField(max_length=200, default='Address Pune')
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=200, default='Address Pune')
