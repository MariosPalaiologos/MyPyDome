from django.contrib import admin

from .models import Product, Offer, Wishlist, Order, ContactForm

from accounts.models import Customer
# Register your models here.

class ProductAdmin(admin.ModelAdmin):  # inheritance me vasikes leitourgies
    list_display = ('name', 'price', 'stock') #TUPLE 


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date_created')

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category','status', 'description', "date_created", 'creator')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'wishlist_item', 'date_created', 'status')


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'change_account_type', 'status']


admin.site.register(Product, ProductAdmin)

admin.site.register(Offer, OfferAdmin)

admin.site.register(Customer, CustomerAdmin)

admin.site.register(Wishlist, WishlistAdmin)

admin.site.register(Order, OrderAdmin)

admin.site.register(ContactForm, ContactFormAdmin)

