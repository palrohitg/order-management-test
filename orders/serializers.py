from rest_framework import serializers
from .models import Order, OrderItem  

class OrderSerializer(serializers.ModelSerializer): 
	class Meta:
		model = Order
		# fields = ('order_number', 'first_name','last_name', 'phone',
		# 		  'email', 'address_line_1', 'address_line_2', 'country'
		# 		  'state', 'city', 'order_note')
		fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer): 
	# orders = OrderSerializer(many=True, read_only=True)
	class Meta:
		model = OrderItem
		fields = "__all__"
	