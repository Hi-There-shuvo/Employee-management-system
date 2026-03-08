from django.db import models
from django.contrib.auth.models import User
from departments.models import Department


class Employee(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    phone = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, related_name='employees'
    )
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    joining_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True
    )

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username}"

    @property
    def full_name(self):
        return self.user.get_full_name() or self.user.username

    @property
    def email(self):
        return self.user.email


class SalaryRecord(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='salary_records'
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    effective_date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-effective_date']

    def __str__(self):
        return f"{self.employee} - {self.amount} ({self.effective_date})"
