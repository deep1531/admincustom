from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# def dashboard(request):
#     categories = Order.objects.all()
#     return render(request,'index.html',{'categories': categories})



def home(request):
    return render(request,'index2.html')


@login_required(login_url='/login_page/')
def order(request):
    if request.method == "POST":
        data = request.POST
        name= data.get('name')
        slug = data.get('slug')
        image = request.FILES.get('image')
        
        
        Order.objects.create(
            name = name,
            slug = slug,
            image = image,
            )
        
       
        return redirect ("/admin/order/")

    abc = Order.objects.all()
    if request.GET.get('search'):
        abc = abc.filter(name__icontains = request.GET.get('search'))
        
    context = {'abc': abc}  
    return render(request, 'category.html', context) 


@login_required(login_url='/login_page/')
def update(request,id):   
    queryset = Order.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        image= request.FILES.get('image')
        name = data.get('name')
        slug= data.get('slug')

        queryset.name = name
        queryset.slug = slug

        if image:
            queryset.image = image

        queryset.save()
        return redirect ("/admin/order/")

    context = {'order': queryset}

    return render (request,"update.html", context)


def delete(request,id):
    queryset = Order.objects.get(id = id)
    queryset.delete()
    return redirect ("/admin/order/")

@login_required(login_url='/login_page/')
def product(request):
    if request.method == "POST":
        data = request.POST
        name= data.get('name')
        slug = data.get('slug')
        image = request.FILES.get('image')
        description = data.get('description')
        price = data.get('price')
        stock = data.get('stock')
        
        Product.objects.create(
            name = name,
            slug = slug,
            image = image,
            description = description,
            price = price,
            stock = stock,
            )
        
       
        return redirect ("/admin/product")

    xyz = Product.objects.all()
    if request.GET.get('search'):
        xyz = xyz.filter(name__icontains = request.GET.get('search'))

    context = {'xyz': xyz}
    
    return render(request,'product.html',context)


@login_required(login_url='/login_page/')
def update_product(request,id):   
    queryset = Product.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        image= request.FILES.get('image')
        name = data.get('name')
        slug= data.get('slug')
        description = data.get('description')
        price = data.get('price')
        stock = data.get('stock')
        

        queryset.name = name
        queryset.slug = slug
        queryset.description = description
        queryset.price = price
        queryset.stock = stock

        if image:
            queryset.image = image

        queryset.save()
        return redirect ("/admin/product")

    context = {'product': queryset}

    return render (request,"update_product.html", context)


def delete_product(request,id):
    queryset = Product.objects.get(id = id)
    queryset.delete()
    return redirect ("/admin/product")



def register(request):

    if request.method == "POST":

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username Already Taken.")
            return redirect ('/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
                    )

        user.set_password(password)
        user.save()
         
        messages.info(request, "Account create successfully.")
        return redirect ('/')

    return render (request, "register.html")



def login_page(request):
    
    if request.method == "POST":
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not User.objects.filter(username=username).exists():
                messages.info(request, "Incorrect Username")
                return redirect ('/login_page')

            user = authenticate(username = username , password = password)

            if user is None :
                messages.info(request, "Incorrect password")
                return redirect ('/login_page')

            else :
                login(request, user)
                return redirect ('/admin/home')


    return render (request, "login.html")

def logout_page(request):
    logout(request)
    return redirect('/login_page/')