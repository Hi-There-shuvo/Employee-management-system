from django import forms
from django.contrib.auth.models import User
from .models import Employee, SalaryRecord


class EmployeeUserForm(forms.ModelForm):
    """Form for creating/editing the User part of an Employee."""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        help_text='Leave blank to keep current password (for editing).',
    )


class EmployeeForm(forms.ModelForm):
    """Form for the Employee profile fields."""
    class Meta:
        model = Employee
        fields = [
            'phone', 'department', 'job_title', 'salary',
            'joining_date', 'status', 'profile_picture',
        ]
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class EmployeeProfileForm(forms.ModelForm):
    """Limited form for employees to update their own profile."""
    class Meta:
        model = Employee
        fields = ['phone', 'profile_picture']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class SalaryRecordForm(forms.ModelForm):
    class Meta:
        model = SalaryRecord
        fields = ['amount', 'effective_date', 'notes']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'effective_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
