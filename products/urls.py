from django.urls import path
from . import views      # Vazw . import giati einai mesa sto fakelo moy


urlpatterns = [
    path('', views.index),
    path('new/', views.new_index),
    path('wishlist/', views.wishlist_index, name='wishlist'),
    path('orders/', views.orders_index, name='orders'),
    path('profile/', views.profile_index),
    path('create_order/', views.createOrder, name="create_order"),
    path('test/', views.test_index, name='test'),
    path('new_item/', views.newWishlistItem, name = 'new_item'),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('update_item/<str:pk>', views.updateWishlistItem, name = 'update_item'),
]