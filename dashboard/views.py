from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count

from accounts.decorators import admin_required
from employees.models import Employee
from departments.models import Department
from attendance.models import Attendance
from leaves.models import Leave


@admin_required
def dashboard(request):
    """Admin dashboard with summary statistics and charts."""
    today = timezone.localdate()

    # Summary stats
    total_employees = Employee.objects.filter(status='active').count()
    total_departments = Department.objects.count()
    on_leave_today = Leave.objects.filter(
        status='approved', start_date__lte=today, end_date__gte=today
    ).count()

    # Today's attendance
    today_attendance = Attendance.objects.filter(date=today)
    today_present = today_attendance.filter(status='present').count()
    today_late = today_attendance.filter(status='late').count()
    today_checked_in = today_attendance.count()

    # Department-wise employee count for chart
    dept_data = Department.objects.annotate(
        emp_count=Count('employees')
    ).values('name', 'emp_count')
    dept_labels = [d['name'] for d in dept_data]
    dept_counts = [d['emp_count'] for d in dept_data]

    # Recent data
    pending_leaves = Leave.objects.filter(
        status='pending'
    ).select_related('employee__user')[:5]

    recent_attendance = Attendance.objects.filter(
        date=today
    ).select_related('employee__user')[:10]

    return render(request, 'dashboard/home.html', {
        'total_employees': total_employees,
        'total_departments': total_departments,
        'on_leave_today': on_leave_today,
        'today_present': today_present,
        'today_late': today_late,
        'today_checked_in': today_checked_in,
        'dept_labels': dept_labels,
        'dept_counts': dept_counts,
        'pending_leaves': pending_leaves,
        'recent_attendance': recent_attendance,
    })
