from django.shortcuts import render

def index(request):
    context = {
        'page_title':'магазин',
    }
    return render(request, 'mainapp/index.html', context)

def contacts(request):
    context = {
        'page_title':'контакты',
    }
    return render(request, 'mainapp/contacts.html', context)

def products(request):
    context = {
        'page_title':'каталог',
    }
    return render(request, 'mainapp/products.html', context)