from django.shortcuts import render


def fake_admin_login(request):
    """Fake admin login page — looks real but always shows 'invalid credentials'."""
    error_message = None
    if request.method == 'POST':
        # Always show error, never actually log in
        error_message = "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."

    return render(request, 'fake_admin/login.html', {
        'error_message': error_message,
    })
