from .models import Payments
from productsapi.models import Products
from users.models import User
from django.core.exceptions import ValidationError
from rest_framework.response import Response

def is_user_have_product(user_id, product_id):
    user = User.objects.get(id=user_id)
    product_exists = user.owned_products.filter(id=product_id).exists()
    if not product_exists:
        raise ValidationError(f"User with ID {user_id} does not have product with ID {product_id}.")


# if product_id exists in Users.owned_products raise error