from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='store_home'),
    path('product/<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('shop/about/', views.about_render, name='about_render'),
    path('shop/faqs/', views.faqs_render, name='faqs_render'),
]