from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin that ensures the user is an admin (is_staff)."""

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, 'You do not have permission to access this page.')
        return redirect('accounts:login')
