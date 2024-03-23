from django.db import models
from users.models import User
from productsapi.models import Products

class Payments(models.Model):
    product_id = models.ForeignKey('productsapi.Products', on_delete=models.CASCADE, verbose_name='Товар')
    seller_id = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Продавец', related_name='payment_seller')
    purchaser_id = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Покупець', related_name='payment_purchaser')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма платежу')