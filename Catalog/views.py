from django.shortcuts import render
from .models import Product, Category

def index(request):

    x = "qweqwe"
    all_category = Category.objects.all()
    all_product = Product.objects.all()

    products = []
    categorys = []

    for product in all_product:
        product_info = {
            'title': product.title,
            'price': product.price,
            'category': product.category,
            'image': product.picture,
            'manufacturer': product.manufacturer,
            'picture': product.picture
        }
        products.append(product_info)

    for category in all_category:
        category_info = {
            'name': category.name
        }
        categorys.append(category_info)


    context = {'all_info_product': products, 'all_info_category': categorys}

    return render(request, 'Score/StartPage.html', context)



