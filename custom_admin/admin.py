from django.contrib import admin
from .models import  CustomUser, ShipmentHistory, Package

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(ShipmentHistory)
admin.site.register(Package)
