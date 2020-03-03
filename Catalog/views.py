from django.shortcuts import render
from .models import Product

def index(request):

    all_product = Product.objects.all()
    products = []

    for product in all_product:
        product_info = {
            'title': product.title,
            'price': product.price,
            'category': product.category
        }
        products.append(product_info)

    context = {'all_info': products}

    return render(request, 'Score/StartPage.html', context)



