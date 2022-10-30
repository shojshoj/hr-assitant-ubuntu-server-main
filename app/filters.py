from cgitb import lookup
from dataclasses import field
import django_filters
from django_filters import CharFilter

from .models import *

class EmployeeFilter(django_filters.FilterSet):
    firstname = django_filters.CharFilter(lookup_expr='icontains')
    lastname = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Employee
        fields = {'lastname','firstname'}