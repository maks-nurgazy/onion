from rest_framework import routers
from .api import UserViewSet, ProductViewSet, SaleViewSet, ClientViewSet, DebtSaleViewSet, DeptPaymentViewSet, \
    SubscriptionViewSet

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'user')
router.register('api/product', ProductViewSet, 'product')
router.register('api/sale', SaleViewSet, 'sale')
router.register('api/client', ClientViewSet, 'client')
router.register('api/debtSale', DebtSaleViewSet, 'debtSale')
router.register('api/deptPayment', DeptPaymentViewSet, 'deptPayment')
router.register('api/subscription', SubscriptionViewSet, 'subscription')

urlpatterns = router.urls
