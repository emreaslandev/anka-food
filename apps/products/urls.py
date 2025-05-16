from django.urls import path
from . import views


urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list'),
    path('<slug:category_slug>/<slug:slug>/', views.product_detail, name='product_detail'),
]
