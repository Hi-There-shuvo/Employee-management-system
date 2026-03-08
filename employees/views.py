from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from accounts.decorators import admin_required
from .models import Employee, SalaryRecord
from .forms import EmployeeForm, EmployeeUserForm, EmployeeProfileForm, SalaryRecordForm
from departments.models import Department


# ── Admin: Employee Management ────────────────────────────────

@admin_required
def employee_list(request):
    """Display all employees with search and filter."""
    queryset = Employee.objects.select_related('user', 'department')

    # select_related performs a SQL JOIN to fetch related 'user' and 'department' 
    # records in a single query, optimizing performance by avoiding N+1 queries 
    # when accessing employee.user or employee.department in the template.

    # Search
    query = request.GET.get('q', '')
    if query:
        queryset = queryset.filter(
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(job_title__icontains=query) |
            Q(user__email__icontains=query)
        )

    # Filters
    department = request.GET.get('department', '')
    if department:
        queryset = queryset.filter(department_id=department)

    status = request.GET.get('status', '')
    if status:
        queryset = queryset.filter(status=status)

    # Pagination
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employees/employee_list.html', {
        'employees': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'departments': Department.objects.all(),
        'current_query': query,
        'current_department': department,
        'current_status': status,
    })





@admin_required
def employee_create(request):
    """Create a new employee with user account."""
    if request.method == 'POST':
        user_form = EmployeeUserForm(request.POST)
        employee_form = EmployeeForm(request.POST, request.FILES)

        if user_form.is_valid() and employee_form.is_valid():
            # Create user
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            user.set_password(password if password else 'defaultpass123')
            user.save()

            # Create employee linked to user
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()

            messages.success(request, f'Employee {employee.full_name} created successfully.')
            return redirect('employees:list')
    else:
        user_form = EmployeeUserForm()
        employee_form = EmployeeForm()

    return render(request, 'employees/employee_form.html', {
        'user_form': user_form,
        'employee_form': employee_form,
        'is_edit': False,
    })


@admin_required
def employee_update(request, pk):
    """Update an existing employee."""
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        user_form = EmployeeUserForm(request.POST, instance=employee.user)
        employee_form = EmployeeForm(request.POST, request.FILES, instance=employee)

        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            employee_form.save()

            messages.success(request, f'Employee {employee.full_name} updated successfully.')
            return redirect('employees:list')
    else:
        user_form = EmployeeUserForm(instance=employee.user)
        employee_form = EmployeeForm(instance=employee)

    return render(request, 'employees/employee_form.html', {
        'user_form': user_form,
        'employee_form': employee_form,
        'employee': employee,
        'is_edit': True,
    })


@admin_required
def employee_detail(request, pk):
    """View employee details."""
    employee = get_object_or_404(Employee.objects.select_related('user', 'department'), pk=pk)
    return render(request, 'employees/employee_detail.html', {
        'employee': employee,
    })


@admin_required
def employee_delete(request, pk):
    """Delete an employee and their user account."""
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.user.delete()  # Cascade deletes Employee too
        messages.success(request, 'Employee deleted successfully.')
        return redirect('employees:list')

    return render(request, 'employees/employee_confirm_delete.html', {
        'employee': employee,
    })


# ── Employee Self-Service ─────────────────────────────────────

@login_required
def my_profile(request):
    """Employee views/updates their own profile."""
    employee = get_object_or_404(Employee, user=request.user)

    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('employees:my_profile')
    else:
        form = EmployeeProfileForm(instance=employee)

    return render(request, 'employees/my_profile.html', {
        'employee': employee,
        'form': form,
    })


# ── Admin: Salary Management ─────────────────────────────────

@admin_required
def salary_list(request):
    """Display all salary records."""
    queryset = SalaryRecord.objects.select_related('employee__user').all()
    paginator = Paginator(queryset, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employees/salary_list.html', {
        'records': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    })


@admin_required
def salary_create(request):
    """Add a salary record for an employee."""
    if request.method == 'POST':
        form = SalaryRecordForm(request.POST)
        if form.is_valid():
            employee_id = request.POST.get('employee')
            employee = get_object_or_404(Employee, pk=employee_id)

            record = form.save(commit=False)
            record.employee = employee
            record.save()

            # Update employee's current salary
            employee.salary = form.cleaned_data['amount']
            employee.save()

            messages.success(request, f'Salary record added for {employee.full_name}.')
            return redirect('employees:salary_list')
    else:
        form = SalaryRecordForm()

    return render(request, 'employees/salary_form.html', {
        'form': form,
        'employees': Employee.objects.select_related('user').all(),
    })


# ── Employee: My Salary ──────────────────────────────────────

@login_required
def my_salary(request):
    """Employee views their own salary records."""
    records = SalaryRecord.objects.filter(employee__user=request.user)
    return render(request, 'employees/my_salary.html', {
        'records': records,
    })
