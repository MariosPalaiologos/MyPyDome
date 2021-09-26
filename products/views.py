from django.http import HttpResponse

from django.shortcuts import render, redirect

from .models import Product, Wishlist, Order, ContactForm   #import ta models

from django.contrib.auth.decorators import login_required # gia na mhn exw prosvash xwris log in

from django.contrib.admin.views.decorators import staff_member_required  #gia eisodo admin
from django.contrib.auth.models import User

from .forms import OrderForm, NewItemForm, NewContactForm, OrderFormUpdate, NewAccountTypeContactForm

from .filters import *

from django.db.models.functions import Lower  # gia to Order BY case insensitive

# Create your views here.
#TI FAINETAI SE KA8E URL REQUEST


#otan kalw /products sto site kanei to index() *****

# Den xrhsimopoieitai kapou to index. Htan sta arxika stadia 

@staff_member_required(login_url='accounts')     #an den eimai staff den exw access
def index(request):                #  gia to products/   

    #return HttpResponse('Hello World')
    # Diavazw ta dedomena mou apo DB
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})  
    #Kalw to arxeio apo to templates, {..}  DICTIONARY


@login_required(login_url='accounts')     #an den exw kane login den exw access
def new_index(request):            # gia to products/new/
    return HttpResponse('Hello World from new')



@staff_member_required(login_url='accounts')     #an den eimai staff den exw access
def wishlist_index(request):                

    #return HttpResponse('Hello World from profile')

    # Diavazw ta dedomena mou apo DB
    wishlist = Wishlist.objects.all().order_by(Lower('name'))    # Emfanizontai me taksinomish me vash to onoma tou proiontos, ordered_by
    orders = Order.objects.all().order_by('customer')           #Emfanizontai me taksinomish me vash ton customer tou order, ordered_by

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs   # neo 'orders' meta so search  

    context={'wishlist': wishlist, 'orders': orders, 'myFilter': myFilter}   #Dictionary
    
    return render(request, 'wishlist.html', context)


@login_required(login_url='accounts')     #an den exw kane login den exw access
def orders_index(request):                #  
    #return HttpResponse('Hi from Orders')
    # Diavazw ta dedomena mou apo DB
    orders = Order.objects.all()

    context = {'orders': orders}
    
    return render(request, 'order.html', context)


@login_required(login_url='accounts')     #an den exw kane login den exw access
def profile_index(request):                #  
    #return HttpResponse('Hi from Orders')

    # Diavazw ta dedomena mou apo DB
    contact_forms = ContactForm.objects.all()
    context = {'contact_forms': contact_forms}
    
    
    return render(request, 'profile.html', context)


@login_required(login_url='accounts')     #an den exw kane login den exw access
def createOrder(request):                #  
    
    form = OrderForm()

    if request.method == 'POST':
        #print('Printing POST: ', request.POST)
        form = OrderForm(request.POST)

        if form.is_valid():
            #form.save()
            #return redirect('orders')
            # obj = form.save(commit=False)
            # obj.customer = User.objects.get(pk=request.user.id)  #gia ton current user
            # obj.save()

            # Otan kanw order, to stock paei -1
            item = form.cleaned_data['wishlist_item']    #pairnw to onoma tou
            product = Wishlist.objects.get(name=item)    #to travaw apo th DB

            if product.stock > 0:  #an den exei stock tou dinw thn epilogh na perimenei apla

                obj = form.save(commit=False)
                obj.customer = User.objects.get(pk=request.user.id)  #gia ton current user
                obj.save()
                product.stock = product.stock - 1    #afairw apo to stock afou ekana order
                product.save()

                return redirect('orders')
            else:
                return redirect('no_stock')     #an den exw stock


    context={'form':form}
    
    return render(request, 'order_form.html', context)


@login_required(login_url='accounts')     #an den exw kane login den exw access
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


@staff_member_required(login_url='accounts')     #an den eimai staff den exw access
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

@staff_member_required(login_url='accounts')     #an den eimai staff den exw access
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


@login_required(login_url='accounts')     #an den exw kane login den exw access
def test_index(request):
    #return HttpResponse('Welcome to PyShop')

    return render(request, 'test.html')


@login_required(login_url='accounts')     #an den exw kane login den exw access
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


@login_required(login_url='accounts')     #an den exw kane login den exw access
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




@login_required(login_url='accounts')   #an den exw kane login den exw access
def pruducts_for_sale(request):

    #return HttpResponse('Hello World from profile')

    products = Wishlist.objects.all().order_by(Lower('name'))
    #products_all = Wishlist.objects.all()
    #products = products_all.exclude(stock='0')  #gia na mhn deixnw dia8esimo me 0 stock

    orders = Order.objects.all()

    myFilter = ProductsForSale(request.GET, queryset=products)
    products = myFilter.qs   # neo 'products' meta so search  

    context={'products': products, 'orders': orders, 'myFilter':myFilter}
    
    return render(request, 'products_for_sale.html', context)



@login_required(login_url='accounts')       #an den exw kane login den exw access
def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('wishlist')

    context={'item':order}
    return render(request, 'delete_order.html', context)


@login_required(login_url='accounts')           #an den exw kane login den exw access
def deleteProduct(request,pk):
    product = Wishlist.objects.get(id=pk)


    #POLY SHMANTIKO
    #AN TO PRODUCT UPARXEI SE ACTIVE ORDER DEN MPORW NA TO SVHSW
    if request.method == 'POST':
        orders = Order.objects.filter(wishlist_item=product.id).exclude(status='Delivered').count()

        if orders > 0:
           return redirect('product_in_order')     # enhmerwnw pws to proion vrisketai se kapoia energh paragkelia
        else:
            product.delete()                       # An oxi, to diagrafw
            return redirect('wishlist')
            

    context={'item':product}
    return render(request, 'delete_product.html', context)



@login_required(login_url='accounts')     #an den exw kane login den exw access
def no_stock(request):
    #return HttpResponse('Welcome to PyShop')

    return render(request, 'no_stock.html')


@login_required(login_url='accounts')     #an den exw kane login den exw access
def product_in_order(request):
    #return HttpResponse('Welcome to PyShop')

    return render(request, 'product_in_order.html')