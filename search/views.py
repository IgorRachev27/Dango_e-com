from django.shortcuts import render
from app.models import Category, Product, Contact_us, Brand

# Create your views here.
def Search(request):
    query = request.GET['query']
    product = Product.objects.filter(name__icontains=query)

    context = {
        'product': product,
    }
    return render(request, 'search.html', context)