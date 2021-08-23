from django.forms import ModelForm
from .models import Order, Wishlist, ContactForm

class OrderForm(ModelForm):
    class Meta:
        model = Order
        #fields = '__all__'   #gia ola ta stoixeia
        #fields = ['wishlist_item', 'status']
        fields = ['wishlist_item']


class OrderFormUpdate(ModelForm):
    class Meta:
        model = Order
        #fields = '__all__'   #gia ola ta stoixeia
        fields = ['wishlist_item', 'status']


class NewItemForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['name', 'price', 'stock', 'category', 'description']


class NewContactForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['message']


class NewAccountTypeContactForm(ModelForm):
    class Meta:
        model = ContactForm
        fields = ['message', 'change_account_type']