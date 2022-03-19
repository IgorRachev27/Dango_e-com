from django.shortcuts import render, redirect
from app.models import Category, Product, Contact_us, Brand
from app.forms import UserCreateForm
from django.contrib.auth import authenticate, login

# чтобы парсить словари в html
from django.template.defaulttags import register
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def Master(request):
    return render(request, 'base.html')

def Index(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('category')
    summ = {}
    for br in brand:
        l = len(Product.objects.filter(brand=br))
        summ[br] = l

    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')
    else:
        product = Product.objects.all()
    context = {
        'category': category,
        'product': product,
        'brand': brand,
        'summ':summ,
    }
    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('index')
    else:
        form = UserCreateForm()

    context={
        'form':form
    }
    return render(request, 'registration/signup.html', context)



def Contact_Page(request):
    if request.POST:
        contact = Contact_us(
        name = request.POST.get('name'),
        email = request.POST.get('email'),
        subject = request.POST.get('subject'),
        message = request.POST.get('message'),
        )
        contact.save()
    return render(request, 'contact.html')


def Product_page(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('category')
    summ = {}
    for br in brand:
        l = len(Product.objects.filter(brand=br))
        summ[br] = l

    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')
    else:
        product = Product.objects.all()
    context = {
        'category': category,
        'product': product,
        'brand': brand,
        'summ':summ,
    }
    return render(request, 'product.html', context)

def Product_detail(request, id):
    product = Product.objects.filter(id=id).first()
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('category')
    summ = {}
    for br in brand:
        l = len(Product.objects.filter(brand=br))
        summ[br] = l

    context = {
        'product':product,
        'category': category,
        'product': product,
        'brand': brand,
        'summ': summ,
    }
    return render(request, 'product_detail.html', context)