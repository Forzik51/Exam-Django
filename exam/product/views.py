from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    data = {
        "items": Product.objects.all(),
        "featured_items": Product.objects.all()[:8],
    }
    return render(request, 'pages/index.html', data)


def contact(request):
    return render(request, 'pages/contact.html')


def normal(request):
    return render(request, 'pages/normal.html')


def faq(request):
    return render(request, 'pages/faq.html')


def product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, 'pages/product.html', context=context)
