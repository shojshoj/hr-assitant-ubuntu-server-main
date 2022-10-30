from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('employee_form', views.employee_form, name='employee_form'),
    path('employee_list', views.employee_list, name='employee_list'),
    path('employee_update/<int:id>', views.employee_update, name='employee_update'),
    path('employee_delete/<int:id>', views.employee_delete, name='employee_delete'),
]