from django.shortcuts import render

from rest_framework import generics
from .models import Coupon
from .serializers import CouponSerializer

from .models import Coupon
from django.utils import timezone, dateformat
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from bson.decimal128 import Decimal128

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class apply_coupon_code(APIView):

    def post(self, request):
        if request.method == 'POST':
            coupon_code = request.data['code']
            print(timezone.now())
            try:
                coupon = Coupon.objects.get(code=coupon_code, expiration_date__gt=timezone.now())
            except Coupon.DoesNotExist:
                return Response({"message": "Invalid or expired coupon code."}, status=status.HTTP_400_BAD_REQUEST)

            #converting str to float
            price = float(request.data['price'])
            #converting Decimal128 to float
            discount_value = float(str(coupon.discount_value))

            # Apply discount logic based on the coupon type (percentage or fixed)
            if coupon.discount_type == 'percentage':
                price-=price*(discount_value/100)
                pass
            elif coupon.discount_type == 'fixed':
                price-=discount_value
                pass
            # Proceed with the checkout process
            return Response({"message": "Coupon code applied successfully.",
                             "new_price":price}, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)