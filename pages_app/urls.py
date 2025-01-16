from django.urls import path

from .views import home_page, dashboard_page, login_page, register_page, products_page, contact_page

urlpatterns = [
    # Home
    path('', home_page, name='home_page'),
    path('contact/', contact_page, name='contact_page'),

    # Auth
    path('auth/login/', login_page, name='login_page'),
    path('auth/register/', register_page, name='register_page'),

    # Dashboard
    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('dashboard/products/', products_page, name='products_page'),
]
