from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminapp.forms import AdminShopUserUpdateForm, AdminShopUserCreateForm, AdminProductCategoryUpdateForm, AdminProductUpdateForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


# @user_passes_test(lambda x: x.is_superuser)
# def index(request):
#     context = {
#         'title': 'пользователи',
#         'shop_users': ShopUser.objects.all().order_by('-is_active', '-is_superuser')
#     }
#     return render(request, 'adminapp/index.html', context)


class ShopUserList(ListView):
    model = ShopUser

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        form = AdminShopUserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = AdminShopUserCreateForm()

    context = {
        'title': 'пользователи/создание',
        'form': form
    }
    return render(request, 'adminapp/user_update.html', context)


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


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    user.is_active = False
    user.save()
    # user.delete()
    return HttpResponseRedirect(reverse('myadmin:index'))


@user_passes_test(lambda u: u.is_superuser)
def productcategories(request):
    context = {
        'title': 'категории продуктов',
        'object_list': ProductCategory.objects.all()
    }
    return render(request, 'adminapp/productcategory_list.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def productcategory_create(request):
#     if request.method == 'POST':
#         form = AdminProductCategoryUpdateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('myadmin:productcategories'))
#     else:
#         form = AdminProductCategoryUpdateForm()

#     context = {
#         'title': 'категории продуктов/создание',
#         'form': form
#     }
#     return render(request, 'adminapp/productcategory_update.html', context)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    success_url = reverse_lazy('myadmin:productcategory')
    form_class = AdminProductCategoryUpdateForm


# @user_passes_test(lambda u: u.is_superuser)
# def productcategory_update(request, pk):
#     obj = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         form = AdminProductCategoryUpdateForm(request.POST, request.FILES, instance=obj)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('myadmin:productcategories'))
#     else:
#         form = AdminProductCategoryUpdateForm(instance=obj)

#     context = {
#         'title': 'категории продуктов/редактирование',
#         'form': form
#     }
#     return render(request, 'adminapp/productcategory_update.html', context)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    success_url = reverse_lazy('myadmin:productcategories')
    # fields = '__all__'
    form_class = AdminProductCategoryUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории\редактирование'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def productcategory_delete(request, pk):
#     obj = get_object_or_404(ProductCategory, pk=pk)
#     obj.is_active = False
#     obj.save()
#     # user.delete()
#     return HttpResponseRedirect(reverse('myadmin:productcategories'))


class ProductCategoryDelete(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('myadmin:productcategories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    objs = category.product_set.all()
    # objs = get_list_or_404(Product, category=pk)
    # category = objs[0].category
    context = {
        'title': f'продукты категории {category.name}',
        'category': category,
        'object_list': objs
    }
    return render(request, 'adminapp/products_list.html', context)

@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = AdminProductUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:products', kwargs={'pk': category.pk}))
    else:
        form = AdminProductUpdateForm(initial = {
            'category': category,
            # 'quantity': 10,
            # 'price': 157.9,
        })

    context = {
        'title': 'продукты/создание',
        'form': form,
        'category': category
    }
    return render(request, 'adminapp/product_update.html', context)

@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = AdminProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(
                'myadmin:products', kwargs={'pk': product.category.pk}))
    else:
        form = AdminProductUpdateForm(instance=product)

    context = {
        'title': 'продукты/редактирование',
        'form': form,
        'category': product.category
    }
    return render(request, 'adminapp/product_update.html', context)

@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        obj.is_active = False
        obj.save()
        return HttpResponseRedirect(reverse(
            'myadmin:products', kwargs={'pk': obj.category.pk}
        ))
    else:
        context = {
            'title': 'продукты/удаление',
            'obj': obj,
        }
        return render(request, 'adminapp/product_delete.html', context)
