from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from accounts.decorators import admin_required
from .models import Department
from .forms import DepartmentForm


@admin_required
def department_list(request):
    """Display all departments."""
    departments = Department.objects.all()
    return render(request, 'departments/department_list.html', {
        'departments': departments,
    })


@admin_required
def department_create(request):
    """Create a new department."""
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department created successfully.')
            return redirect('departments:list')
    else:
        form = DepartmentForm()

    return render(request, 'departments/department_form.html', {
        'form': form,
        'is_edit': False,
    })


@admin_required
def department_update(request, pk):
    """Update an existing department."""
    department = get_object_or_404(Department, pk=pk)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department updated successfully.')
            return redirect('departments:list')
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'departments/department_form.html', {
        'form': form,
        'department': department,
        'is_edit': True,
    })


@admin_required
def department_delete(request, pk):
    """Delete a department."""
    department = get_object_or_404(Department, pk=pk)

    if request.method == 'POST':
        department.delete()
        messages.success(request, 'Department deleted successfully.')
        return redirect('departments:list')

    return render(request, 'departments/department_confirm_delete.html', {
        'department': department,
    })
