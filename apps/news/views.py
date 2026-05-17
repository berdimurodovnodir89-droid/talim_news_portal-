import feedparser

from django.shortcuts import render



def home(request):

    feed = feedparser.parse(
        "https://kun.uz/news/rss"
    )

    latest_news = []

    for item in feed.entries[:12]:

        latest_news.append({
            'title': item.title,
            'summary': item.summary,
            'published': item.published,
        })

    context = {
        'latest_news': latest_news
    }

    return render(
        request,
        'news/home.html',
        context
    )



def get_news_by_keyword(keyword):

    feed = feedparser.parse(
        "https://kun.uz/news/rss"
    )

    items = []

    for item in feed.entries:

        title = item.title.lower()

        summary = ""

        if hasattr(item, 'summary'):
            summary = item.summary.lower()

        if keyword in title or keyword in summary:

            items.append({
                'title': item.title,
                'summary': item.summary if hasattr(item, 'summary') else '',
                'published': item.published,
            })

    return items



def talim_news(request):

    items = get_news_by_keyword("ta'lim")

    context = {
        'items': items,
        'page_title': "Ta'lim Yangiliklari"
    }

    return render(
        request,
        'news/talim.html',
        context
    )



def texno_news(request):

    items = get_news_by_keyword("texnologiya")

    context = {
        'items': items,
        'page_title': "Texnologiya Yangiliklari"
    }

    return render(
        request,
        'news/texno.html',
        context
    )



def sport_news(request):

    items = get_news_by_keyword("sport")

    context = {
        'items': items,
        'page_title': "Sport Yangiliklari"
    }

    return render(
        request,
        'news/sport.html',
        context
    )



def jahon_news(request):

    items = get_news_by_keyword("jahon")

    context = {
        'items': items,
        'page_title': "Jahon Yangiliklari"
    }

    return render(
        request,
        'news/jahon.html',
        context
    )

def detail(request):

    return render(
        request,
        'news/detail.html'
    )
def detail(request, slug):

    return render(
        request,
        'news/detail.html'
    )
def category_news(request, slug):

    items = get_news_by_keyword(slug)

    return render(
        request,
        'news/category.html',
        {
            'items': items,
            'page_title': slug.upper()
        }
    )