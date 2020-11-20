from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from .serializer import ProductsListSerializer


class ProductsList(APIView):

    def get(self, request, format=None):
        dishes = models.Product.objects.all()
        serializer = ProductsListSerializer(dishes, context={'request': request}, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get_object(self, pk):
        try:
            return models.Product.objects.get(pk=pk)
        except models.Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsListSerializer(product, context={'request': request})
        return Response(serializer.data)
