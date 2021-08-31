from django.urls import path
from . import views      # Vazw . import giati einai mesa sto fakelo moy


urlpatterns = [
    path('', views.index),
    path('new/', views.new_index),
    path('wishlist/', views.wishlist_index, name='wishlist'),
    path('orders/', views.orders_index, name='orders'),
    path('profile/', views.profile_index, name='profile'),
    path('create_order/', views.createOrder, name="create_order"),
    path('test/', views.test_index, name='test'),
    path('new_item/', views.newWishlistItem, name = 'new_item'),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('update_item/<str:pk>', views.updateWishlistItem, name = 'update_item'),
    path('contact_form/', views.contact_form, name='contact_form'),
    path('products/', views.pruducts_for_sale, name='_products_for_sale'),
    path('change_account_type/', views.change_account_type, name='change_account_type'),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
    path('no_stock/', views.no_stock, name='no_stock'),
    path('product_in_order/', views.product_in_order, name='product_in_order'),
    path('delete_product/<str:pk>', views.deleteProduct, name="delete_product"),
]