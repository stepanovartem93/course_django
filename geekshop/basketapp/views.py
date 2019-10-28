from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from basketapp.models import Basket
from geekshop.settings import LOGIN_URL
from mainapp.models import Product
from mainapp.views import get_basket


def index(request):
    context = {
        'basket': get_basket(request),
    }
    return render(request, 'basketapp/index.html', context)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if not Basket.objects.filter(user=request.user, product=product).exists():
    
        Basket.objects.create(user=request.user, product=product, quantity=1)

    else:
    
        obj = Basket.objects.filter(user=request.user, product=product).first()
        obj.quantity += 1
        obj.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_delete(request, pk):
    get_object_or_404(Product, pk=pk).delete()
    # return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect(reverse('basket:index'))