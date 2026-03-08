from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('check-in/', views.check_in, name='check_in'),
    path('check-out/', views.check_out, name='check_out'),
    path('my-attendance/', views.my_attendance, name='my_attendance'),
    path('all/', views.admin_attendance, name='admin_attendance'),
]
