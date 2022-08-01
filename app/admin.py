from django.contrib import admin
from app.models import ProductApp, Order, Basket

# Register your models here.
admin.site.register(ProductApp)
admin.site.register(Order)
admin.site.register(Basket)
