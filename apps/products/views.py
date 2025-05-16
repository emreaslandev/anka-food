from django.shortcuts import render, get_object_or_404
from . models import Product, Category

def category_list(request):
    categories = Category.objects.all().order_by('order')
    context = {
        'categories': categories
    }
    return render(request, 'pages/product_categories.html', context)

def product_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(is_active=True).order_by('order')
    categories = Category.objects.all().order_by('order')
    context = {
        'products': products,
        'categories': categories,
        'category': category

    }
    return render(request, 'pages/products.html', context)

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, category__slug=category_slug)
    products = Product.objects.all().order_by('order')
    category = product.category  # Bunu ekleyin

    context = {
        'product': product,
        'products': products,
        'category': category,  # Bunu ekleyin
    }

    return render(request, 'details/product_detail.html', context)