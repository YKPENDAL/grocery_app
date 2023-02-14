from django.shortcuts import render, redirect
from .models import Product,Order
from .views import Product
from django.contrib.auth.models import User, auth
from .forms import PostForm
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'index.html')


def veg(request):
    prods = Product.objects.filter(type='v')
    return render(request, 'veg.html', {'prods': prods})


def fruit(request):
    prods1 = Product.objects.filter(type='f')
    return render(request, 'fruit.html', {'prods': prods1})


def personalcare(request):
    prods2 = Product.objects.filter(type='p')
    return render(request, 'personalcare.html', {'prods': prods2})


def snack(request):
    prods3 = Product.objects.filter(type='s')
    return render(request, 'snack.html', {'prods': prods3})


def householditem(request):
    prods4 = Product.objects.filter(type='h')
    return render(request, 'householditem.html', {'prods': prods4})


def admin(request):
    return render(request, 'admin/')


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Username is not available')
                return redirect('post_new')
            elif User.objects.filter(email=email).exists():
                messages.success(request, 'Email is already in use!!')
                return redirect('post_new')

            elif form.is_valid():

                user = User.objects.create_user(
                    username=username, password=password, first_name=first_name, last_name=last_name)
                post = form.save(commit=False)

                post.save()
                user.save()

                messages.success(request, 'You have registered successfully!!!')
            return redirect('login')

        else:
            messages.success(request, 'Password is not matching!')
        return redirect('post_new')

    else:
        form = PostForm()
        return render(request, 'post_edit.html', {'form': form})

def contact(request):
    return render (request,'contact.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')

        else:
            messages.success(request, 'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def myacct(request):
    return render(request, 'myacct.html')


def checkout(request):

    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pincode = request.POST.get('pincode', '')
                

        order = Order(items_json=items_json, first_name=first_name, last_name=last_name,email=email, address=address, city=city, state=state, pincode=pincode, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})
    return render(request, 'checkout.html')
