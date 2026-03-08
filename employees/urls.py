from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    # Admin employee management
    path('', views.employee_list, name='list'),
    path('create/', views.employee_create, name='create'),
    path('<int:pk>/', views.employee_detail, name='detail'),
    path('<int:pk>/update/', views.employee_update, name='update'),
    path('<int:pk>/delete/', views.employee_delete, name='delete'),

    # Employee self-service
    path('my-profile/', views.my_profile, name='my_profile'),
    path('my-salary/', views.my_salary, name='my_salary'),

    # Salary management (admin)
    path('salary/', views.salary_list, name='salary_list'),
    path('salary/create/', views.salary_create, name='salary_create'),
]
