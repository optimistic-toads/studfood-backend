from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models
from .serializer import MainDishesSerializer


# TODO: return image url!
class DishesList(APIView):

    def get(self, request, format=None):
        dishes = models.MainDish.objects.all()
        serializer = MainDishesSerializer(dishes,context={'request': request}, many=True)
        return Response(serializer.data)
