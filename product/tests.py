from django.test import TestCase
from models import Product, Promotion

# Create your tests here.
class TestProduct(TestCase):
    def setUp(self):
        Product.objects.acreate(name="Product 1", price=20, all=50)
        Promotion.objects.acreate(name="Promotion 1", description="The promotion for Product 1", price=30,)