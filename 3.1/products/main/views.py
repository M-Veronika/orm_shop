from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer

from main.models import Product, Review


@api_view(['GET'])
def products_list_view(request):
    products_list = ProductListSerializer(Product.objects.all(), many=True).data
    return Response(products_list)  
   #""реализуйте получение всех товаров из БД
   # реализуйте сериализацию полученных данных
   # отдайте отсериализованные данные в Response"""

class ProductDetailsView(APIView):
    def get(self, request, product_id):
        product = ProductDetailsSerializer(Product.objects.get(id=product_id)).data
        return Response(product)
        #""реализуйте получение товара по id, если его нет, то выдайте 404
        #реализуйте сериализацию полученных данных
        #отдайте отсериализованные данные в Response"""


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
