# from django.db import models
from djongo import models

from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Coupon(models.Model):
    code = models.CharField(max_length=10)
    discount_type = models.CharField(max_length=10, choices=[('percentage', 'Percentage'), ('fixed', 'Fixed')])
    discount_value = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    expiration_date = models.DateTimeField()