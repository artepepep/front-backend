from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    is_active = models.BooleanField(default=True)
    country = models.CharField(max_length=105)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    owned_products = models.ManyToManyField('productsapi.Products', related_name='have_prod')
    REGISTRATION_CHOICES = [
        ('email', 'Email'),
        ('google', 'Google'),
    ]
    registration_method = models.CharField(
        max_length=10,
        choices=REGISTRATION_CHOICES,
        default='email'
    )
    REQUIRED_FIELDS = ["country", "city", "phone_number", "email"]

    def __str__(self):
       return self.username