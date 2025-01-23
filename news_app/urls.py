from django.urls import path

from .views import all_news_page, news_detail_page

urlpatterns = [
    path('', all_news_page, name='all_news_page'),
    path('<int:pk>/', news_detail_page, name='news_detail_page'),
]

