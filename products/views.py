from django.http import HttpResponse

from django.shortcuts import render

from .models import Product   #import to model product

from django.contrib.auth.decorators import login_required # gia na mhn exw prosvash xwris log in


# Create your views here.
#TI FAINETAI SE KA8E URL REQUEST


#otan kalw /products sto site 8elw na kanlei to index() *****

@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def index(request):                #  gia to products/

    #return HttpResponse('Hello World')

    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})  
    #Kalw to arxeio apo to templates, {..}  DICTIONARY


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def new_index(request):            # gia to new/
    return HttpResponse('Hello World from new')


