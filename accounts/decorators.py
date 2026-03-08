from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def admin_required(view_func):
    """Decorator that ensures the user is an admin (is_staff)."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        if not request.user.is_staff:
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('accounts:login')
        return view_func(request, *args, **kwargs)
    return wrapper
