from django.shortcuts import render
from . models import About
from apps.features.models import Feature
from apps.brands.models import Brand

def about(request):
    abouts = About.objects.filter(is_active=True).order_by('order')
    features = Feature.objects.filter(is_active=True).order_by('order')
    brands = Brand.objects.filter(is_active=True).order_by('order')

    context = {
        'abouts': abouts,
        'features': features,
        'brands': brands,
    }

    return render(request, 'pages/about.html', context)
