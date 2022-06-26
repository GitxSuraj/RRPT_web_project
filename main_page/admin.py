from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Order, OrderUpdate, JobApplication, TShirts, Trousers

admin.site.register(Product)
admin.site.register(Trousers)
admin.site.register(TShirts)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
admin.site.register(JobApplication)
