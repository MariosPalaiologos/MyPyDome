from django.db import models

from django.conf import settings

#from accounts.models import Customer

from django.contrib.auth.models import User

# Create your models here. gia thn DB mas


class Product(models.Model):     #inherit apo Model class toy DJANGO
# Pairnei polla etoima xaraktiristika

    name = models.CharField(max_length=255)   # 255 characters, to vazw gia prostasia
    price = models.FloatField()
    stock = models.IntegerField()
    image_urls = models.CharField(max_length=2083) # Tupiko mege8os enos URL


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Wishlist(models.Model):
    CATEGORY = (
        ('Groceries', 'Groceries'),
        ('Food', 'Food'),
        ('Clothing-Apparel', 'Clothing-Apparel'),
        ('Household', 'Household'),
        ('Appliances', 'Appliances'),
        ('Electronics', 'Electronics'),
        ('Gaming', 'Gaming'),
        ('Computer Parts', 'Computer Parts'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    stock = models.IntegerField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    #creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(
            ('Pending Approval', 'Pending Approval'),
            ('Out of Stock', 'Out of Stock'),
            ('Ordered', 'Ordered'),
            ('Delivering', 'Delivering'),
            ('Delivered', 'Delivered')
    )

    #sysxetish me to model Customer
    customer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    wishlist_item = models.ForeignKey(Wishlist, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, default='Pending Approval', choices=STATUS)

    def __str__(self):
        return self.wishlist_item.name


class ContactForm(models.Model):
    ACCOUNT_STATUS=(
                    ('Company', 'Company'),
                    ('Customer', 'Customer'),
                    ('No', 'No')
    )
    STATUS = (
              ('Sent', 'Sent'),
              ('Being Reviewed','Being Reviewed'),
              ('Finished', 'Finished')
    )
    name = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    message = models.CharField(max_length=250, null=True)
    change_account_type = models.CharField(max_length=200, default='No', choices=ACCOUNT_STATUS)
    status = models.CharField(max_length=200, default='Sent', choices=STATUS)