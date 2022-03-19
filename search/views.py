from django.shortcuts import render
from app.models import Category, Product, Contact_us, Brand

# Create your views here.
def Search(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('category')
    summ = {}
    for br in brand:
        l = len(Product.objects.filter(brand=br))
        summ[br] = l


    query = request.GET['query']

    product = Product.objects.filter(name__icontains=query)
    context = {
        'category': category,
        'product': product,
        'brand': brand,
        'summ': summ,
    }
    return render(request, 'search.html', context)