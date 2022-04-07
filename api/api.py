from rest_framework import viewsets, permissions

from api.serializers import UserSerializer, ProductSerializer, ClientSerializer, DebtSaleSerializer, \
    DeptPaymentSerializer, SubscriptionSerializer
from client.models import Client
from debt_payment.models import DeptPayment
from debt_sale.models import DebtSale
from product.models import Product
from sale.models import Sale
from subscription.models import Subscription
from user.models import Users


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClientSerializer


class DebtSaleViewSet(viewsets.ModelViewSet):
    queryset = DebtSale.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DebtSaleSerializer


class DeptPaymentViewSet(viewsets.ModelViewSet):
    queryset = DeptPayment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DeptPaymentSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubscriptionSerializer
