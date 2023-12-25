from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)

    products_images_pajamas = products_images.filter(product__category__id=2)

    context = {
        'products_images': products_images,
        'products_images_pajamas': products_images_pajamas,
    }
    return render(request, 'landing/home.html', context=context)
