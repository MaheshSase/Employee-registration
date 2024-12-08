from django.shortcuts import render,redirect,get_object_or_404
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.

# @login_required
def create_employee(request):
    if request.method=='POST':
        form= EmployeeForm(request.POST)
        if form.is_valid():
            emp=form.save(commit=False)
            # emp.user = request.user
            emp.save()
            return redirect('emp_list')
    else:
        form=EmployeeForm()
        print(form)
    return render (request,'meesho/create_employee.html ',{'form': form})

# @login_required

def emp_list(request):
    emps = Employee.objects.all()
    return render(request,'meesho/emp_list.html',{'emps':emps})

# @login_required
def emp_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_login')
    else:
        form = UserCreationForm()
    return render(request, 'meesho/emp_register.html', {'form': form})

# @login_required

def emp_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('emp_list')
    else:
        form = AuthenticationForm()
    return render(request, 'meesho/emp_login.html', {'form': form})

# @login_required
def emp_delete(request,pk):
    emp = get_object_or_404(Employee,pk=pk)
    emp.delete()
    return redirect('emp_list')

# @login_required
def emp_update(request,pk):
    emp = get_object_or_404(Employee , pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
        return redirect('emp_list')
    else:
        form = EmployeeForm(instance=emp)
    return render(request, 'meesho/create_employee.html',{'form': form})

# @login_required
def emp_logout(request):
    auth_logout(request)
    return redirect('emp_login')
