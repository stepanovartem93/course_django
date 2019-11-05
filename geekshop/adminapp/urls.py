"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.index, name='index'),
    re_path(r'^user/create/$', adminapp.user_create, name='user_create'),
    re_path(r'^user/update/(?P<pk>\d+)$', adminapp.user_update, name='user_update'),
    re_path(r'^user/delete/(?P<pk>\d+)$', adminapp.user_delete, name='user_delete'),

    re_path(r'^productcategories/$', adminapp.productcategories, name='productcategories'),
    re_path(r'^productcategory/create/$', adminapp.productcategory_create, name='productcategory_create'),
    re_path(r'^productcategory/update/(?P<pk>\d+)/$', adminapp.productcategory_update, name='productcategory_update'),
    re_path(r'^productcategory/delete/(?P<pk>\d+)/$', adminapp.productcategory_delete, name='productcategory_delete'),
    
    re_path(r'^products/(?P<pk>\d+)/$', adminapp.products, name='products'),
    re_path(r'^products/create/(?P<pk>\d+)/$', adminapp.product_create, name='product_create'),
    re_path(r'^products/update/(?P<pk>\d+)/$', adminapp.product_update, name='product_update'),
]
