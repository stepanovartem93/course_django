from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from authapp.forms import ShopUserLoginForm
from authapp.forms import ShopUserRegisterForm


def user_login(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ShopUserLoginForm()

    context = {
        'title': 'вход в систему',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)

def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

def user_register(request):
    title = 'регистрация'
    
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:user_login'))
    
    else:
        register_form = ShopUserRegisterForm()

    content = {
        'title' : 'регистрация в системе',
         'register_form': register_form,
         }

    return render(request, 'authapp/register.html', content)

def user_update(request):
    return HttpResponseRedirect(reverse('main:index'))