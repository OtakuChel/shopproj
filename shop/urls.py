
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='landing/home.html'), name='home'),
    path('/123/', include('landing.urls')),
    path('/products/', include('products.urls')),
    path('/orders/', include('orders.urls')),
]
