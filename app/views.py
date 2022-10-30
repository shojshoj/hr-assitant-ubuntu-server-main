from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, EmployeeForm
from .models import *
from .filters import EmployeeFilter
from django.db.models import Q


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    employees = Employee.objects.all()
    total_employees = employees.count()
    total_male = employees.filter(gender='Male').count()
    total_female = employees.filter(gender='Female').count()
    total_trainee = employees.filter(position='Trainee').count()
    total_senior = employees.filter(position='Senior Developer').count()
    total_junior = employees.filter(position='Junior Developer').count()
    total_nss = employees.filter(position='Network Support Specialist').count()
    total_sa = employees.filter(position='System Analyst').count()
    total_ued = employees.filter(position='User Experience Designer').count()
    total_ds = employees.filter(position='Data Scientist').count()
    total_da = employees.filter(position='Database Administrator').count()
    total_full_time = employees.filter(emp_type='Full-Time').count()
    total_part_time = employees.filter(emp_type='Part-Time').count()
    total_temporary = employees.filter(emp_type='Temporary').count()
    total_seasonal = employees.filter(emp_type='Seasonal').count()
    total_active = employees.filter(status='Active').count()
    total_on_leave = employees.filter(status='On-leave').count()
    total_suspended = employees.filter(status='Suspended').count()
    total_terminated = employees.filter(status='Terminated').count()
    total_male_trainee = employees.filter(gender='Male', position='Trainee').count()
    total_female_trainee = employees.filter(gender='Female', position='Trainee').count()
    total_male_senior = employees.filter(gender='Male', position='Senior Developer').count()
    total_female_senior = employees.filter(gender='Female', position='Senior Developer').count()
    total_male_junior = employees.filter(gender='Male', position='Junior Developer').count()
    total_female_junior = employees.filter(gender='Female', position='Junior Developer').count()
    total_male_nss = employees.filter(gender='Male', position='Network Support Specialist').count()
    total_female_nss = employees.filter(gender='Female', position='Network Support Specialist').count()
    total_male_sa = employees.filter(gender='Male', position='System Analyst').count()
    total_female_sa = employees.filter(gender='Female', position='System Analyst').count()
    total_male_ued = employees.filter(gender='Male', position='User Experience Designer').count()
    total_female_ued = employees.filter(gender='Female', position='User Experience Designer').count()
    total_male_ds = employees.filter(gender='Male', position='Data Scientist').count()
    total_female_ds = employees.filter(gender='Female', position='Data Scientist').count()
    total_male_da = employees.filter(gender='Male', position='Database Administrator').count()
    total_female_da = employees.filter(gender='Female', position='Database Administrator').count()

    context = { 'employees': employees, 
                'total_employees': total_employees,
                'total_male': total_male, 
                'total_female': total_female,
                'total_trainee': total_trainee,
                'total_senior': total_senior,
                'total_junior': total_junior,
                'total_nss': total_nss,
                'total_sa': total_sa,
                'total_ued': total_ued,
                'total_ds': total_ds,
                'total_da': total_da,
                'total_full_time': total_full_time,
                'total_part_time': total_part_time,
                'total_temporary': total_temporary,
                'total_seasonal': total_seasonal,
                'total_active': total_active,
                'total_on_leave': total_on_leave,
                'total_suspended': total_suspended,
                'total_terminated': total_terminated,
                'total_male_trainee': total_male_trainee,
                'total_female_trainee': total_female_trainee,
                'total_male_senior': total_male_senior,
                'total_female_senior': total_female_senior,
                'total_male_junior': total_male_junior,
                'total_female_junior': total_female_junior,
                'total_male_nss': total_male_nss,
                'total_female_nss': total_female_nss,
                'total_male_sa': total_male_sa,
                'total_female_sa': total_female_sa,
                'total_male_ued': total_male_ued,
                'total_female_ued': total_female_ued,
                'total_male_ds': total_male_ds,
                'total_female_ds': total_female_ds,
                'total_male_da': total_male_da,
                'total_female_da': total_female_da}
    return render(request, 'dashboard.html', context)
 
@login_required(login_url='login')
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, request.FILES,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee_list')

@login_required(login_url='login')
def employee_list(request):
    employee_list = Employee.objects.all()

    filter = EmployeeFilter(request.GET, queryset=employee_list)
    employee_list = filter.qs

    context = {'employee_list':employee_list, 'filter': filter}
    return render(request, 'employee_list.html', context)

@login_required(login_url='login')
def employee_update(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, request.FILES,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee_list')
    
@login_required(login_url='login')
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('/employee_list')

    context = {'employee':employee}
    return render(request, 'employee_delete.html', context)