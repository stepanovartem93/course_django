from django.shortcuts import render
from mainapp.models import ProductCategory, Product

def index(request):
    context = {
        'page_title':'магазин',
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
    }
    return render(request, 'mainapp/contacts.html', context)

def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {
        'page_title': 'каталог',
        'categories_menu': categories,
        'products': products,
    }
    return render(request, 'mainapp/products.html', context)