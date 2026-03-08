from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator

from accounts.decorators import admin_required
from employees.models import Employee
from .models import Attendance


# ── Employee: Check In / Check Out ────────────────────────────

@login_required
def check_in(request):
    """Employee checks in for the day."""
    if request.method == 'POST':
        employee = get_object_or_404(Employee, user=request.user)
        today = timezone.localdate()
        now = timezone.localtime().time()

        attendance, created = Attendance.objects.get_or_create(
            employee=employee, date=today,
            defaults={'check_in': now, 'status': 'present'}
        )

        if not created:
            messages.warning(request, 'You have already checked in today.')
        else:
            from datetime import time
            if now > time(9, 0):
                attendance.status = 'late'
                attendance.save()
                messages.info(request, f'Checked in at {now.strftime("%I:%M %p")} (Late)')
            else:
                messages.success(request, f'Checked in at {now.strftime("%I:%M %p")}')

    return redirect('attendance:my_attendance')


@login_required
def check_out(request):
    """Employee checks out for the day."""
    if request.method == 'POST':
        employee = get_object_or_404(Employee, user=request.user)
        today = timezone.localdate()
        now = timezone.localtime().time()

        try:
            attendance = Attendance.objects.get(employee=employee, date=today)
            if attendance.check_out:
                messages.warning(request, 'You have already checked out today.')
            else:
                attendance.check_out = now
                attendance.save()
                messages.success(request, f'Checked out at {now.strftime("%I:%M %p")}')
        except Attendance.DoesNotExist:
            messages.error(request, 'You need to check in first.')

    return redirect('attendance:my_attendance')


# ── Employee: My Attendance ───────────────────────────────────

@login_required
def my_attendance(request):
    """Employee views their own attendance history."""
    employee = get_object_or_404(Employee, user=request.user)
    today = timezone.localdate()

    queryset = Attendance.objects.filter(employee=employee).order_by('-date')
    today_record = Attendance.objects.filter(employee=employee, date=today).first()

    paginator = Paginator(queryset, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'attendance/my_attendance.html', {
        'attendances': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'today_record': today_record,
        'employee': employee,
    })


# ── Admin: All Attendance ─────────────────────────────────────

@admin_required
def admin_attendance(request):
    """Admin views all attendance records with search and filters."""
    queryset = Attendance.objects.select_related('employee__user').order_by('-date')

    # Search
    query = request.GET.get('q', '')
    if query:
        queryset = queryset.filter(
            Q(employee__user__first_name__icontains=query) |
            Q(employee__user__last_name__icontains=query)
        )

    # Filters
    status = request.GET.get('status', '')
    if status:
        queryset = queryset.filter(status=status)

    date_filter = request.GET.get('date', '')
    if date_filter:
        queryset = queryset.filter(date=date_filter)

    paginator = Paginator(queryset, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'attendance/admin_attendance.html', {
        'attendances': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'current_query': query,
        'current_status': status,
        'current_date': date_filter,
    })
