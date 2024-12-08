from django.urls import path
from.import views


urlpatterns = [
    path('create/',views.create_employee,name="create_employee"),
    path('Emp_list/',views.emp_list,name='emp_list'),
    path('Emp_register/',views.emp_register,name="emp_register"),
    path('Emp_login/',views.emp_login, name="emp_login"),
    path('update/<int:pk>/',views.emp_update,name="emp_update"),
    path('delete/<int:pk>/',views.emp_delete,name="emp_delete"),
    path('Emp_logout/',views.emp_logout, name = "emp_logout")
    
]

# 8000/meesho/Create_employee