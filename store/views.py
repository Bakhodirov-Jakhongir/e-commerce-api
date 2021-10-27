from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer 

# Create your views here.

@api_view()
def product_list(request):

    query_set = Product.objects.all()
    serializer = ProductSerializer(query_set , many=True)
    return Response(serializer.data)

@api_view()
def product_detail(request , id):
    product = get_object_or_404(Product,pk=id)
    try:
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)