from django.shortcuts import render,redirect, reverse
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.views.decorators.http import require_http_methods


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    # product_entries = Product.objects.filter(user=request.user)
    
    context = {
        'nama_aplikasi' : 'karesu',
        'nama': request.user.username,
        'kelas': 'PBP B',
    }

    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Step 1: Check if only username is entered (not password yet)
        if username and not password:
            # Check if the username exists in the database
            try:
                user_exists = User.objects.get(username=username)
                context = {'username': username}
                return render(request, 'login.html', context)
            except User.DoesNotExist:
                messages.error(request, 'This username does not exist.')
                return render(request, 'login.html')
        
        # Step 2: Username exists, now check the password
        elif username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse('main:show_main'))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.error(request, 'Invalid password.')
                context = {'username': username}
                return render(request, 'login.html', context)
        else:
            messages.error(request, 'This username does not exist.')

    return render(request, 'login.html')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Product.objects.get(pk=id)

    # Set product entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def show_products(request):
    product_entries = Product.objects.filter(user=request.user)  
    # # Rename this to product_entries
    context = {
        'product_entries': product_entries  
        # # Change 'products' to 'product_entries'
    }
    return render(request, "products.html", context)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    name = strip_tags(request.POST.get("product_name"))
    price = request.POST.get("product_price")
    description = strip_tags(request.POST.get("product_description"))
    user = request.user
    new_product = Product(name=name, price=price, description=description, user=user)
    new_product.save()
    
    return HttpResponse(b"CREATED", status=201)

@require_http_methods(["DELETE"])
def delete_product_ajax(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponse(b"DELETED", status=201)


        
