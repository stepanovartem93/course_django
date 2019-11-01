from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import AdminShopUserUpdateForm
# , AdminShopUserCreateForm, AdminProductCategoryUpdateForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    context = {
        'title': 'пользователи',
        'shop_users': ShopUser.objects.all().order_by('-is_active', '-is_superuser')
    }
    return render(request, 'adminapp/index.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        form = AdminShopUserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = AdminShopUserUpdateForm(instance=user)

    context = {
        'title': 'пользователи/редактирование',
        'form': form
    }
    return render(request, 'adminapp/user_update.html', context)


def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    user.is_active = False
    user.save()
    # user.delete()
    return HttpResponseRedirect(reverse('myadmin:index'))