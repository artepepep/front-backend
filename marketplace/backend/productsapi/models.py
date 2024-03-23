from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категорія продукту')
    owned_subcategorys = models.ManyToManyField('productsapi.Subcategory')
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Products(models.Model):
    publication_date = models.DateTimeField(default=timezone.now)
    product_name = models.CharField(max_length=255, verbose_name='Назва продукту')
    product_description = models.TextField(verbose_name='Опис продукту')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія продукту')
    product_subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Підкатегорія продукту')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна продукту')
    product_quantity = models.IntegerField(verbose_name='Кількість продукту')
    product_images = models.ImageField(upload_to='product_images/')
    product_tags = models.ManyToManyField(Tag)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='who_sell')

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'

class Basket(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='basket_owner')
    products = models.ManyToManyField('productsapi.Products', related_name='products_in_basket')