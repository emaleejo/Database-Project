from django.contrib import admin

# Register your models here.
from .models import (Book, Author, Category, ContactDetail,
                     Address, Email, Order, OrderItem,
                     Phone, Supplier, SupplierRep, Review)

admin.site.site_header = 'Ivancic\'s Library [ADMIN]'

# admin.site.register(database)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(ContactDetail)
admin.site.register(Address)
admin.site.register(Email)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Phone)
admin.site.register(Supplier)
admin.site.register(SupplierRep)
admin.site.register(Review)
