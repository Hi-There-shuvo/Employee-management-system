from django.db import models
from employees.models import Employee


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('late', 'Late'),
        ('absent', 'Absent'),
    ]

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='attendances'
    )
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='present')

    class Meta:
        ordering = ['-date']
        unique_together = ['employee', 'date']

    def __str__(self):
        return f"{self.employee} - {self.date} ({self.status})"
