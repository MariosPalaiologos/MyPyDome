from django.urls import path
from . import views      # Vazw . import giati einai mesa sto fakelo moy

urlpatterns = [
    path('', views.account_index, name='accounts'),
    path('login/', views.login_index, name='login'),
    path('register/', views.register_index, name='register'),
    path('logout/', views.logout_user_index, name='logout')
]