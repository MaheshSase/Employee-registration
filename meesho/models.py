from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_code = models.CharField(max_length=150)
    emp_department = models.CharField(max_length=200)
    emp_status = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.emp_name
