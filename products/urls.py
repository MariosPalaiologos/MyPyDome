from django.urls import path
from . import views      # Vazw . import giati einai mesa sto fakelo moy


urlpatterns = [
    path('', views.index),
    path('new/', views.new_index),
]