from django.forms import ModelForm
from .models import Order, Wishlist

class OrderForm(ModelForm):
    class Meta:
        model = Order
        #fields = '__all__'   #gia ola ta stoixeia
        fields = ['wishlist_item', 'status']


class NewItemForm(ModelForm):
    class Meta:
        model = Wishlist
        fields = ['name', 'price', 'category', 'description']