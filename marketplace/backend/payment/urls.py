from django.urls import path
from .views import payment_page, PaymentsAPI

urlpatterns = [
    path('payment-page/', payment_page),
    path('payments/', PaymentsAPI.as_view(), name='get-create-payments'),
]