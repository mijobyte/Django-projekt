import random

from django.db import transaction
from django.core.management.base import BaseCommand

from ducan.models import Customer, Product, Order, OrderItem, ShippingAddress
from ducan.factory import (
    CustomerFactory,
    ProductFactory,
    OrderFactory,
    OrderItemFactory,
    ShippingAddressFactory
)

NUM_CUSTOMERS = 10
NUM_PRODUCTS = 100
NUM_ORDERS = 5
NUM_ORDERITEMS = 10
NUM_SHIPPINGADDRESSES = 5

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Customer, Product, Order, OrderItem, ShippingAddress]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_CUSTOMERS):
            author = CustomerFactory()

        for _ in range(NUM_PRODUCTS):
            book = ProductFactory()

        for _ in range(NUM_ORDERS):
            book = OrderFactory()

        for _ in range(NUM_ORDERITEMS):
            book = OrderItemFactory()

        for _ in range(NUM_SHIPPINGADDRESSES):
            book = ShippingAddressFactory()
