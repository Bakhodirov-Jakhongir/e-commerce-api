from rest_framework import serializers
from decimal import Decimal
from store.models import Product , Collection


class CollectionSerializer(serializers.Serializer):
     id = serializers.IntegerField()
     title = serializers.CharField()

class ProductSerializer(serializers.Serializer):
     id = serializers.IntegerField()
     title = serializers.CharField(max_length=255)
     price = serializers.DecimalField(max_digits=6,decimal_places=2 ,source='unit_price')
     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

     #relations of models in serializer
     #Primary key
     # collection = serializers.PrimaryKeyRelatedField(
     #      queryset = Collection.objects.all()
     # )
     #String 
     # collection = serializers.StringRelatedField()
     #Nested Objects
     # collection = CollectionSerializer()
     #Relationships via HyperLink
     collection = serializers.HyperlinkedRelatedField(view_name='collection_detail' , queryset = Collection.objects.all())

     def calculate_tax(self , product:Product):
          return product.unit_price * Decimal(1.1);

