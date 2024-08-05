from django.contrib import admin
from .models import Invoice, Item, Address

# Register your models here.

admin.site.register(Invoice)
admin.site.register(Address)
admin.site.register(Item)
