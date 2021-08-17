from django.http import HttpResponse

from django.shortcuts import render, redirect

from .models import Product, Wishlist, Order   #import to model product

from django.contrib.auth.decorators import login_required # gia na mhn exw prosvash xwris log in

from .forms import OrderForm

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



@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def wishlist_index(request):                # 

    #return HttpResponse('Hello World from profile')

    #current_user = request.user
    #name = current_user.id

    #wishlist = Wishlist.objects.get(creator_id = current_user.id)
    wishlist = Wishlist.objects.all()
    
    return render(request, 'wishlist.html', {'wishlist': wishlist})


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def orders_index(request):                #  
    #return HttpResponse('Hi from Orders')
    
    orders = Order.objects.all()
    
    return render(request, 'order.html', {'orders': orders})


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def profile_index(request):                #  
    #return HttpResponse('Hi from Orders')
    
    
    return render(request, 'profile.html')


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def createOrder(request):                #  
    
    form = OrderForm()

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')


    context={'form':form}
    
    return render(request, 'order_form.html', context)
