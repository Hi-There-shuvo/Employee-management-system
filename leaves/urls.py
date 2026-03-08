from django.urls import path
from . import views

app_name = 'leaves'

urlpatterns = [
    path('apply/', views.leave_apply, name='apply'),
    path('my-leaves/', views.my_leaves, name='my_leaves'),
    path('all/', views.admin_leave_list, name='admin_list'),
    path('<int:pk>/<str:action>/', views.leave_action, name='action'),
]
