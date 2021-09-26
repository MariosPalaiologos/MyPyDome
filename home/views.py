from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required # gia na mhn exw prosvash xwris log in


# Create your views here.

@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw kai me paei sto accounts
def home_index(request):
    #return HttpResponse('Welcome to PyShop')

    return render(request, 'home.html')