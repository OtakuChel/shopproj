from django.shortcuts import render

from products.models import Product


def product(request, product_id: int):
    product = Product.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    context = {
        'product': product,
        'session_key': session_key
    }


    return render(request, 'products/product.html', context=context)
