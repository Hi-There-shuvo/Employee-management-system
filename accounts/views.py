from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm


def login_view(request):
    """Handle user login with role-based redirect."""
    # If already logged in, redirect based on role
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('dashboard:home')
        return redirect('employees:my_profile')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('dashboard:home')
            return redirect('employees:my_profile')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """Handle user logout (POST only)."""
    if request.method == 'POST':
        logout(request)
    return redirect('accounts:login')


@login_required
def password_change_view(request):
    """Handle password change."""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep user logged in
            messages.success(request, 'Password changed successfully!')
            return redirect('accounts:password_change_done')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'accounts/password_change.html', {'form': form})


@login_required
def password_change_done_view(request):
    """Show password change success page."""
    return render(request, 'accounts/password_change_done.html')
