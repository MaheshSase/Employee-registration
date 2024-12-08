from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields='__all__'
        # fields =['emp_name','emp_code','emp_department','emp_status']