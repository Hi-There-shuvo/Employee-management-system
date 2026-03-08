from django.contrib import admin
from .models import Employee, SalaryRecord


class SalaryRecordInline(admin.TabularInline):
    model = SalaryRecord
    extra = 0


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'department', 'job_title', 'status')
    list_filter = ('status', 'department')
    search_fields = ('user__first_name', 'user__last_name', 'user__email')
    inlines = [SalaryRecordInline]


@admin.register(SalaryRecord)
class SalaryRecordAdmin(admin.ModelAdmin):
    list_display = ('employee', 'amount', 'effective_date')
    list_filter = ('effective_date',)
