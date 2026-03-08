from django import forms
from .models import Leave


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['leave_type', 'start_date', 'end_date', 'reason']
        widgets = {
            'leave_type': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class LeaveActionForm(forms.Form):
    """Form for admin to approve/reject leave."""
    admin_remarks = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        required=False,
    )
