import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Package(models.Model):
    CARRIER = [
        ('DHL', 'DHL'),
        ('FedEx', 'FexEx'),
        ('UPS', 'UPS'),
        ('EDS', 'EDS'),
    ]

    SHIPMENT_MEDIUM = [
        ('Road', 'Road'),
        ('Ship', 'Ship'),
        ('Flight', 'Flight'),
    ]

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    tracking_id = models.CharField(max_length=200, unique=True)
    carrier = models.CharField(max_length=20, choices=CARRIER)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=400)
    state = models.CharField(max_length=300)
    origin = models.CharField(max_length=100, help_text='Country of origin')
    destination = models.CharField(max_length=100, help_text='Country of destination')
    weight = models.PositiveIntegerField(help_text='(LBS.)')
    length = models.PositiveIntegerField(help_text='(IN.)')
    width = models.PositiveIntegerField(help_text='(IN.)')
    height = models.PositiveIntegerField(help_text='(IN.)')
    quantity = models.IntegerField()
    freight_cost = models.DecimalField(decimal_places=3, max_digits=20)
    shipment_medium = models.CharField(max_length=300, choices=SHIPMENT_MEDIUM)
    pickup_date = models.DateField()
    pickup_time = models.TimeField()

    def __str__(self):
        return self.name


class ShipmentHistory(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Pre-Transit', 'Pre-Transit'),
        ('In transit', 'In transit'),
        ('Out for delivery', 'Out for delivery'),
        ('On Hold', 'On Hold'),
        ('Delivered', 'Delivered'),
    ]

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    package = models.ForeignKey(to=Package, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=300, choices=STATUS, default=STATUS[0][1])
    date = models.DateField()
    time = models.TimeField()
    remarks = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.package.name} -> {self.location}'
