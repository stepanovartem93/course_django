from django.db import models

from authapp.models import ShopUser
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(ShopUser, verbose_name='пользователь', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='товар', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
    