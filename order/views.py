from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order
from products.models import Product
from .serializer import OrderSerializer


class OrderView(APIView):

    def get(self, request):
        snippets = Order.objects.all()
        serializer = OrderSerializer(snippets, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        product = request.POST.get('product')
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(order_saved)})
