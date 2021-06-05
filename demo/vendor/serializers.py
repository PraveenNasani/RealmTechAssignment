from vendor.models import Category, Items, Vendor
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
            model = Items
            fields = ['id', 'item_name']


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'items']



class VendSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Vendor
        fields = ['shop_name', 'category']
