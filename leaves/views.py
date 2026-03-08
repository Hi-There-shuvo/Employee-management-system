from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from accounts.decorators import admin_required
from employees.models import Employee
from .models import Leave
from .forms import LeaveForm, LeaveActionForm


# ── Employee: Apply for Leave ─────────────────────────────────

@login_required
def leave_apply(request):
    """Employee submits a leave application."""
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = get_object_or_404(Employee, user=request.user)
            leave.save()
            messages.success(request, 'Leave application submitted successfully.')
            return redirect('leaves:my_leaves')
    else:
        form = LeaveForm()

    return render(request, 'leaves/leave_form.html', {'form': form})


# ── Employee: My Leaves ───────────────────────────────────────

@login_required
def my_leaves(request):
    """Employee views their own leave history."""
    queryset = Leave.objects.filter(employee__user=request.user).order_by('-applied_on')
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'leaves/my_leaves.html', {
        'leaves': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    })


# ── Admin: All Leave Requests ─────────────────────────────────

@admin_required
def admin_leave_list(request):
    """Admin views all leave requests with status filter."""
    queryset = Leave.objects.select_related('employee__user').order_by('-applied_on')

    status = request.GET.get('status', '')
    if status:
        queryset = queryset.filter(status=status)

    paginator = Paginator(queryset, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'leaves/admin_leave_list.html', {
        'leaves': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'current_status': status,
    })


# ── Admin: Approve / Reject Leave ─────────────────────────────

@admin_required
def leave_action(request, pk, action):
    """Admin approves or rejects a leave request."""
    if request.method == 'POST':
        leave = get_object_or_404(Leave, pk=pk)

        if action not in ('approve', 'reject'):
            messages.error(request, 'Invalid action.')
            return redirect('leaves:admin_list')

        form = LeaveActionForm(request.POST)
        if form.is_valid():
            leave.status = 'approved' if action == 'approve' else 'rejected'
            leave.admin_remarks = form.cleaned_data.get('admin_remarks', '')
            leave.save()
            messages.success(request, f'Leave request {leave.status} for {leave.employee.full_name}.')

    return redirect('leaves:admin_list')
