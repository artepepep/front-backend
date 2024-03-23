from rest_framework import generics
from .models import Products, Basket
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response

class GetAllProductsAPI(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class GetFixAmountProductsAPI(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        quantity = self.kwargs.get('quantity', None)
        if quantity is not None:
            return Products.objects.all()[:quantity]
        return Products.objects.none()

class CreateProductAPI(generics.CreateAPIView):
    queryset = Products.objects.none()
    serializer_class = CreateProductSerializer
    permission_classes = (IsAuthenticated, )

class ProductDetailAPI(generics.RetrieveDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )

class ProductSearchAPI(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        keyword = self.kwargs['keyword']
        return Products.objects.filter(product_name__icontains=keyword)

class GetBasketAPI(APIView):
    # queryset = Basket.objects.all()
    # serializer_class = BasketSerializer
    # permission_classes = (IsAuthenticated, )

    def get(self, request):
        baskets = Basket.objects.all()
        serialized_data = BasketSerializer(baskets, many=True).data
        return Response({'baskets': serialized_data})

class PutBasketAPI(APIView):
    permission_classes = (IsAuthenticated, )
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        
        try:
            instance = Basket.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        
        serializer = PutBasketSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

class CategoryAPI(APIView):
    permission_classes = (AllowAny, )

    def get(self, requests):
        categorys = Category.objects.all()
        serialized_data = CategorySerializer(categorys, many=True).data
        return Response({'categorys': serialized_data})