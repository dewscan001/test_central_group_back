from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name="product_name", max_length=255)
    price = models.DecimalField(verbose_name="product_price", decimal_places=2, max_digits=10)
    all = models.IntegerField(verbose_name="all")

    def __str__(self):
        return self.name

class Promotion(models.Model):
    name = models.CharField(verbose_name="promotion_name", max_length=255)
    description = models.TextField(verbose_name="promotion_description")
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    active = models.BooleanField(verbose_name="is_active")

    def __str__(self):
        return self.name
    