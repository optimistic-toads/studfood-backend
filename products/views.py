from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from .serializer import ProductsSerializer


class ProductsList(APIView):

    def get(self, request, format=None):
        dishes = models.Product.objects.all()
        serializer = ProductsSerializer(dishes, context={'request': request}, many=True)
        return Response(serializer.data)
