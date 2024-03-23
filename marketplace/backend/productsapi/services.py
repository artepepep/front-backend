from .models import Products

def add_commission(price, percent):
    percent *= 0.01
    new_amount = float(price) + (float(price) * percent)
    return float(new_amount)

# def validate_product_ownership(product_id, user):
#     if Products.objects.filter(id=product_id, user=user).exists():
#         raise ValidationError("This product already has an owner")