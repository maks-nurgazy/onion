from rest_framework import serializers

from debt_payment.models import DeptPayment
from debt_sale.models import DebtSale
from product.models import Product
from sale.models import Sale
from subscription.models import Subscription
from user.models import Users
from client.models import Client


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class DebtSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtSale
        fields = '__all__'


class DeptPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeptPayment
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
