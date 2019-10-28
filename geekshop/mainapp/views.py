import random
from django.shortcuts import render
from mainapp.models import ProductCategory, Product

def get_basket(request):
    if request.user.is_authenticated:
        return request.user.basket_set.all()
    return []

def get_categories_menu():
    return ProductCategory.objects.all()


def get_hot_product():
    return random.choice(Product.objects.all())


def get_same_products(product):
    return product.category.product_set.exclude(pk=product.pk)


def index(request):
    context = {
        'page_title':'магазин',
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    locations = [
        {
            'city': 'Москва',
            'phone':  '+7 987 654 32 10',
            'adress':  'ул. Ленина, д. 2',
            'email':  'contact.msk@myshop.ru',
        },
        {
            'city': 'Санкт-Петербург',
            'phone':  '+7 987 654 32 10',
            'adress':  'ул. Петровская наб., д. 3',
            'email':  'contact.spb@myshop.ru',
        },
        {
            'city': 'Екатеринбург',
            'phone':  '+7 987 654 32 10',
            'adress':  'ул. Б. Ордынка, д. 4',
            'email':  'contact.ekb@myshop.ru', 
        },
    ]
    context = {
        'page_title':'контакты',
        'locations':locations,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/contacts.html', context)


def products(request):
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {
        'page_title': 'каталог',
        'categories_menu': get_categories_menu,
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),
        'basket':get_basket(request),
    }
    return render(request, 'mainapp/products.html', context)


def categories(request, pk):
    products = Product.objects.all()
    context = {
        'page_title': 'каталог',
        'categories_menu': categories,
        'products': products,
        'basket':get_basket(request),
    }
    return render(request, 'mainapp/products.html', context)