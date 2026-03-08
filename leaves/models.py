from django.db import models
from employees.models import Employee


class Leave(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('sick', 'Sick Leave'),
        ('casual', 'Casual Leave'),
        ('annual', 'Annual Leave'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='leaves'
    )
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    admin_remarks = models.TextField(blank=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-applied_on']

    def __str__(self):
        return f"{self.employee} - {self.get_leave_type_display()} ({self.status})"

    @property
    def duration(self):
        return (self.end_date - self.start_date).days + 1
