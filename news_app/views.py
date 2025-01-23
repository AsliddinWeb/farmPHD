from django.shortcuts import render, get_object_or_404

from .models import News

def all_news_page(request):
    all_news = News.objects.all()

    ctx = {
        'all_news': all_news,
    }
    return render(request, 'news/all-news.html', ctx)

def news_detail_page(request, pk):
    new = get_object_or_404(News, pk=pk)

    ctx = {
        'new': new,
    }
    return render(request, 'news/news-detail.html', ctx)
