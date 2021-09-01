from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from .models import Order, Product
from .serializers import OrderSerializer


class OrderListView(APIView):
    """
       Lists all the orders 
    """

    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OrderDetailsView(APIView):
    """
        Retreive, Update and delete by order_numbers 
    """

    def get_objects(self, order_number):
        try:
            return Order.objects.get(order_number=order_number)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, order_number, format=None):
        order = self.get_objects(order_number)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, order_number, format=None):
        order = self.get_objects(order_number)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, order_number, format=None):
        blog = self.get_objects(order_number)
        serializer = Order(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_number, format=None):
        order = self.get_objects(order_number)
        order.delete()
        return Response({"message" : "order is delete"}, status.HTTP_204_NO_CONTENT)