from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order
from products.models import Product
from datetime import datetime
from .serializer import OrderPostSerializer, OrderGetSerializer
from rest_framework.permissions import IsAuthenticated


class OrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        snippets = Order.objects.filter(user=request.user).all()
        serializer = OrderGetSerializer(snippets, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        product = request.POST.get('product')
        serializer = OrderPostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save(user=self.request.user, created_date=datetime.now())
        return Response({"success": order_saved.pk})
