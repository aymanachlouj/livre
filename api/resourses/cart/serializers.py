from rest_framework import serializers
from book_shelf.models import Cart

class CartSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    books = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Cart
        fields = ['user_name', 'books', 'created_at']
