from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from .views import fake_admin_login

urlpatterns = [
    path('matha/', admin.site.urls),              # Real admin (hidden)
    path('admin/', fake_admin_login, name='fake_admin'),  # Fake admin (honeypot)
    path('accounts/', include('accounts.urls')),
    path('employees/', include('employees.urls')),
    path('departments/', include('departments.urls')),
    path('attendance/', include('attendance.urls')),
    path('leaves/', include('leaves.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', lambda request: redirect('accounts:login')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
