from django.urls import path

from .views import (home_page, dashboard_page, login_page, register_page, products_page,
                    contact_page, add_product_page, edit_product_page, delete_product_page,
                    all_products_page, farm_products_page, about_page, farms_page)

urlpatterns = [
    # Home
    path('', home_page, name='home_page'),
    path('contact/', contact_page, name='contact_page'),
    path('products/', all_products_page, name='all_products_page'),
    path('products/<int:pk>/', farm_products_page, name='farm_products_page'),
    path('about/', about_page, name='about_page'),
    path('farms/', farms_page, name='farms_page'),

    # Auth
    path('auth/login/', login_page, name='login_page'),
    path('auth/register/', register_page, name='register_page'),

    # Dashboard
    path('dashboard/', dashboard_page, name='dashboard_page'),

    path('dashboard/products/', products_page, name='products_page'),
    path('dashboard/add-product/', add_product_page, name='add_product_page'),
    path('dashboard/edit-product/<int:pk>/', edit_product_page, name='edit_product_page'),
    path('dashboard/delete-product/<int:pk>/', delete_product_page, name='delete_product_page'),
]
