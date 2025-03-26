from rest_framework import serializers
from main.models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'mark']
    
        # реализуйте все поля
    pass


class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title # реализуйте поля title и price
    pass


class ProductDetailsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'reviews']
        

    def __str__(self):
        return self.title
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    pass
