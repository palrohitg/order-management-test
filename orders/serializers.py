from rest_framework import serializers
from .models import Order, Product  

class OrderSerializer(serializers.ModelSerializer): 
	class Meta:
		model = Order
		fields = '__all__' 