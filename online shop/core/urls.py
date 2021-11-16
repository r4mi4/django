from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('accounts.urls', namespace='accounts')),
                  path('cart/', include('cart.urls', namespace='cart')),
                  path('orders/', include('orders.urls', namespace='orders')),
                  path('', include('shop.urls', namespace='shop')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
