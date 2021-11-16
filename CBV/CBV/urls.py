from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first.urls', namespace='first')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
