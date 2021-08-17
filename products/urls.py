from django.urls import path
from . import views      # Vazw . import giati einai mesa sto fakelo moy


urlpatterns = [
    path('', views.index),
    path('new/', views.new_index),
    path('wishlist/', views.wishlist_index, name='wishlist'),
    path('orders/', views.orders_index, name='orders'),
    path('profile/', views.profile_index),
    path('create_order', views.createOrder, name="create_order")
]