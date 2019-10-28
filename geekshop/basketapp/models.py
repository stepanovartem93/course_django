from django.db import models

from authapp.models import ShopUser
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(ShopUser, verbose_name='пользователь', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='товар', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
    
    def product_cost(self):
        return self.product.price * self.quantity

    def total_price(self):
        return sum(map(
            lambda x:x[0] * x[1], 
            self.user.basket_set.values_list('quantity', 'product__price'))
        )

    def total_quantity(self):
        return sum(self.user.basket_set.values_list('quantity', flat=True))