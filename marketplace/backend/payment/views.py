from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PaymentSerializer
from .services import is_user_have_product
from .models import Payments
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

def payment_page(request):
    template_name = 'payment/payment-page.html'
    return render(request, template_name)

class PaymentsAPI(generics.ListCreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer
    
    def create(self, request, *args, **kwargs):
        purchaser_id = request.data.get('purchaser_id')
        product_id = request.data.get('product_id')
        seller_id = request.data.get('seller_id')
        if purchaser_id == seller_id:
            return Response({"error": "seller can not be a purchaser"})
        else:
            is_user_have_product(seller_id, product_id)
            return super().create(request, *args, **kwargs)
    permission_classes = (IsAuthenticated, )