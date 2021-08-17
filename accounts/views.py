from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required # gia na mhn exw prosvash xwris log in

from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

# Create your views here.


def account_index(request):            # gia to acoounts/

    if request.user.is_authenticated:  # gia na mhn mporw na paw sto log in page otan eimai hdh mesa
        return redirect("home")
    else:
    #return HttpResponse('Hello World from accounts')
        return render(request, 'account.html')



def login_index(request):            # gia to log in/
    #return HttpResponse('Hello World from log in')

    if request.user.is_authenticated:  # gia na mhn mporw na paw sto log in page otan eimai hdh mesa
        return redirect("home")
    else:
        if request.method == 'POST':
            username =request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/home')  #kanw log in kai paw HOME PAGE
            else:
                messages.info(request, "Username OR password is incorrect")
                

        context = {}
        return render(request, 'login.html', context)


def register_index(request):            # gia to register/

    if request.user.is_authenticated:  # gia na mhn mporw na paw sto log in page otan eimai hdh mesa
        return redirect("home")
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')    #paw sto login afou kanw register

        context = {'form':form}
        #return HttpResponse('Hello World from register')
        return render(request, 'register.html', context)


def logout_user_index(request):
    logout(request)
    return redirect('/accounts')
