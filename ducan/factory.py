## factories.py
import factory
from factory.django import DjangoModelFactory
import random

from ducan.models import *

factory.Faker._DEFAULT_LOCALE = 'en_US'

## Defining a factory
class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker("first_name")
    email = factory.Faker("email")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    price = factory.LazyAttribute(lambda x: random.randrange(0, 10000))

class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    customer = factory.Iterator(Customer.objects.all())
    date_ordered = factory.Faker("date_time")
    transaction_id = factory.LazyAttribute(lambda x: random.randrange(0, 10000))

class OrderItemFactory(DjangoModelFactory):
    class Meta:
        model = OrderItem

    product = factory.Iterator(Product.objects.all())
    order = factory.Iterator(Order.objects.all())
    quantity = factory.LazyAttribute(lambda x: random.randrange(0, 10000))
    date_added = factory.Faker("date_time")

class ShippingAddressFactory(DjangoModelFactory):
    class Meta:
        model = ShippingAddress

    customer = factory.Iterator(Customer.objects.all())
    order = factory.Iterator(Order.objects.all())
    address = factory.Faker("address")
    city = factory.Faker("word")
    zipcode = factory.LazyAttribute(lambda x: random.randrange(0, 10000))
    date_added = factory.Faker("date_time")


