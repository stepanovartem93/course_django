from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from geekshop.settings import LOGIN_URL
from mainapp.models import Product
from mainapp.views import get_basket


@login_required
def index(request):
    context = {
        'basket': get_basket(request),
    }
    return render(request, 'basketapp/index.html', context)


@login_required
def basket_add(request, pk):
    if LOGIN_URL in request.META['HTTP_REFERER']:
            return HttpResponseRedirect(
                reverse('main:product', kwargs={'pk': pk})
            )

    product = get_object_or_404(Product, pk=pk)

    if not Basket.objects.filter(user=request.user, product=product).exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        obj = Basket.objects.filter(user=request.user, product=product).first()
        obj.quantity += 1
        obj.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_delete(request, pk):
    get_object_or_404(Basket, pk=pk).delete()
    # return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect(reverse('basket:index'))

def basket_update(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        basket_obj = get_object_or_404(Basket, pk=pk)
        if quantity == 0:
            basket_obj.delete()
        else:
            basket_obj.quantity = quantity
            basket_obj.save()

        basket = get_basket(request)

        context = {
            'basket': basket,
        }
        basket_as_html = render_to_string(
            'basketapp/includes/inc__basket_list.html',
            context=context,
            request=request
        )

        return JsonResponse({
            # 'basket': basket,
            'result': basket_as_html
        })