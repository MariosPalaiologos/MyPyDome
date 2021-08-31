import django_filters
from django_filters import DateFilter, NumberFilter, CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['date_created']


class ProductsForSale(django_filters.FilterSet):

    #start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    # gte = gtreater than equal

    #end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    # lte = less than equal

    product = CharFilter(field_name = "name", lookup_expr='icontains')
    #min_price = NumberFilter(field_name = "price", lookup_expr='gt')
    max_price = NumberFilter(field_name = "price", lookup_expr='lt')
    

    class  Meta:
        model = Wishlist
        fields = '__all__'
        exclude = ['name', 'stock', 'description', 'date_created', 'price']
