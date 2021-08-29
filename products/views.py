from django.http import HttpResponse

from django.shortcuts import render, redirect

from .models import Product, Wishlist, Order, ContactForm   #import to model product

from django.contrib.auth.decorators import login_required # gia na mhn exw prosvash xwris log in

from django.contrib.admin.views.decorators import staff_member_required  #gia eisodos admin
from django.contrib.auth.models import User

from .forms import OrderForm, NewItemForm, NewContactForm, OrderFormUpdate, NewAccountTypeContactForm

from .filters import *

# Create your views here.
#TI FAINETAI SE KA8E URL REQUEST


#otan kalw /products sto site 8elw na kanlei to index() *****

@staff_member_required(login_url='accounts')     #an den eimai staff de mporw na mpw
def index(request):                #  gia to products/

    #return HttpResponse('Hello World')

    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})  
    #Kalw to arxeio apo to templates, {..}  DICTIONARY


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def new_index(request):            # gia to new/
    return HttpResponse('Hello World from new')



@staff_member_required(login_url='accounts')     #an den eimai staff de mporw na mpw
def wishlist_index(request):                # 

    #return HttpResponse('Hello World from profile')

    wishlist = Wishlist.objects.all()
    orders = Order.objects.all()
    context={'wishlist': wishlist, 'orders': orders}
    
    return render(request, 'wishlist.html', context)


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def orders_index(request):                #  
    #return HttpResponse('Hi from Orders')
    
    orders = Order.objects.all()

    myFilter = OrderFilter()   # gia search

    context = {'orders': orders, 'myFilter': myFilter}
    
    return render(request, 'order.html', context)


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def profile_index(request):                #  
    #return HttpResponse('Hi from Orders')

    contact_forms = ContactForm.objects.all()
    context = {'contact_forms': contact_forms}
    
    
    return render(request, 'profile.html', context)


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
            obj.customer = User.objects.get(pk=request.user.id)  #gia ton current user
            obj.save()
            return redirect('orders')


    context={'form':form}
    
    return render(request, 'order_form.html', context)


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def updateOrder(request, pk):  

    order = Order.objects.get(id=pk)
    form = OrderFormUpdate(instance=order)       #gia na parw ta dedomena tou curr Order

    if request.method == 'POST':
        form = OrderFormUpdate(request.POST, instance=order)
        if form.is_valid():
            form.save()
            #return redirect('orders')
            # obj = form.save(commit=False)
            # obj.customer = User.objects.get(pk=request.user.id) #gia ton current user
            # obj.save()
            return redirect('wishlist')

    context={'form':form}
    return render(request, 'order_form.html', context)


@staff_member_required(login_url='accounts')     #an den eimai staff de mporw na mpw
def newWishlistItem(request):                #  
    
    form = NewItemForm()

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = NewItemForm(request.POST)
        if form.is_valid():
            #form.save()
            #return redirect('orders')
            obj = form.save(commit=False)
            obj.creator = User.objects.get(pk=request.user.id)  #gia ton current user
            obj.save()
            return redirect('wishlist')


    context={'form':form}
    
    return render(request, 'new_item_form.html', context)

@staff_member_required(login_url='accounts')     #an den eimai staff de mporw na mpw
def updateWishlistItem(request, pk):

    item = Wishlist.objects.get(id=pk)
    form = NewItemForm(instance=item)          #gia na parw ta dedomena tou current item 

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = NewItemForm(request.POST, instance=item)
        if form.is_valid():
            #form.save()
            #return redirect('orders')
            obj = form.save(commit=False)
            obj.creator = User.objects.get(pk=request.user.id)  #gia ton current user
            obj.save()
            return redirect('wishlist')

    context={'form':form}
    return render(request, 'new_item_form.html', context)


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def test_index(request):
    #return HttpResponse('Welcome to PyShop')

    return render(request, 'test.html')


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def contact_form(request):

    form = NewContactForm()

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = NewContactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = User.objects.get(pk=request.user.id)  #gia ton current user
            obj.save()
            return redirect('profile')


    context={'form':form}

    return render(request, 'contact_form.html', context)


@login_required(login_url='accounts')     #an den exw kane login de mporw na mpw
def change_account_type(request):

    form = NewAccountTypeContactForm()

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = NewAccountTypeContactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = User.objects.get(pk=request.user.id)  #gia ton current user
            obj.save()
            return redirect('profile')


    context={'form':form}

    return render(request, 'change_account_type.html', context)




@login_required(login_url='accounts')
def pruducts_for_sale(request):

    #return HttpResponse('Hello World from profile')

    products = Wishlist.objects.all()
    #products_all = Wishlist.objects.all()
    #products = products_all.exclude(stock='0')  #gia na mhn deixnw dia8esimo me 0 stock

    orders = Order.objects.all()

    myFilter = ProductsForSale(request.GET, queryset=products)
    products = myFilter.qs   # neo 'products' meta so search  

    context={'products': products, 'orders': orders, 'myFilter':myFilter}
    
    return render(request, 'products_for_sale.html', context)



@login_required(login_url='accounts')
def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('wishlist')

    context={'item':order}
    return render(request, 'delete_order.html', context)