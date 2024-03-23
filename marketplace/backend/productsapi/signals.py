from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *
from decimal import Decimal

@receiver(post_save, sender=Products)
def add_product_to_user(sender, instance, **kwargs):
    """
    добавляем созданый продукт выбраному пользователю
    """
    user = instance.user
    user.owned_products.add(instance)

    """
    добавляем комиссию к цене продукта
    """
    commission_rate = Decimal('0.05')
    new_price = instance.product_price + (instance.product_price * commission_rate)
    Products.objects.filter(pk=instance.pk).update(product_price=new_price)

# @receiver(post_save, sender=Subcategory)
# def add_subcategory_to_category(sender, instance, **kwargs):
#     """
#     добавляем подкатегорию к категории
#     """
#     category = instance.f_k
#     category.owned_subcategorys.add(instance)