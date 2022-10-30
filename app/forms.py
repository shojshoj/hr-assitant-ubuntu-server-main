from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Employee

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('firstname', 'lastname', 'age', 'mobile', 'image', 'gender', 'position', 'status', 'emp_type')