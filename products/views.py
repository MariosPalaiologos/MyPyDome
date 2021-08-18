from django.http import HttpResponse

from django.shortcuts import render, redirect

from .models import Product, Wishlist, Order   #import to model product

from django.contrib.auth.decorators import login_required # gia na mhn exw prosvash xwris log in

from django.contrib.admin.views.decorators import staff_member_required  #gia eisodos admin
from django.contrib.auth.models import User

from .forms import OrderForm, NewItemForm

# Create your views here.
#TI FAINETAI SE KA8E URL REQUEST


#otan kalw /products sto site 8elw na kanlei to index() *****

@staff_member_required(login_url='accounts')     #an den exw kane login de mporw na mpw
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
            #form.save()
            #return redirect('orders')
            obj = form.save(commit=False)
            obj.customer = User.objects.get(pk=request.user.id)
            obj.save()
            return redirect('orders')


    context={'form':form}
    
    return render(request, 'order_form.html', context)


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def updateOrder(request, pk):  

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            #form.save()
            #return redirect('orders')
            obj = form.save(commit=False)
            obj.customer = User.objects.get(pk=request.user.id)
            obj.save()
            return redirect('orders')

    context={'form':form}
    return render(request, 'order_form.html', context)


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def newWishlistItem(request):                #  
    
    form = NewItemForm()

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = NewItemForm(request.POST)
        if form.is_valid():
            #form.save()
            #return redirect('orders')
            obj = form.save(commit=False)
            obj.creator = User.objects.get(pk=request.user.id)
            obj.save()
            return redirect('wishlist')


    context={'form':form}
    
    return render(request, 'new_item_form.html', context)

@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def updateWishlistItem(request, pk):

    item = Wishlist.objects.get(id=pk)
    form = NewItemForm(instance=item)

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = NewItemForm(request.POST, instance=item)
        if form.is_valid():
            #form.save()
            #return redirect('orders')
            obj = form.save(commit=False)
            obj.creator = User.objects.get(pk=request.user.id)
            obj.save()
            return redirect('wishlist')

    context={'form':form}
    return render(request, 'new_item_form.html', context)


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def test_index(request):
    #return HttpResponse('Welcome to PyShop')

    return render(request, 'test.html')
