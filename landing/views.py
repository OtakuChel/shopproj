from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)

    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)

    context = {
        'products_images': products_images,
        'products_images_phones': products_images_phones,
        'products_images_laptops': products_images_laptops,
    }
    return render(request, 'landing/home.html', context=context)
