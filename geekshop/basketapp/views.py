from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    pass


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if not Basket.objects.filter(user=request.user, product=product).exists():
    
        Basket.objects.create(user=request.user, product=product, quantity=1)

    else:
    
        obj = Basket.objects.filter(user=request.user, product=product).first()
        obj.quantity += 1
        obj.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

