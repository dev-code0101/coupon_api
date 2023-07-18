from django.urls import path, include
from .views import CouponViewSet, apply_coupon_code
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CouponViewSet)

urlpatterns = [
    path('apply/', apply_coupon_code.as_view(), name='apply-coupon'),
    path('',include(router.urls))
]
