import feedparser
from django.shortcuts import render


def get_news(url):

    feed = feedparser.parse(url)

    news = []

    for item in feed.entries:

        image = ""

        try:
            image = item.media_content[0]["url"]
        except:
            image = "https://picsum.photos/600/400"

        news.append({
            "title": item.get("title", "Sarlavha mavjud emas"),
            "description": item.get("summary", "Ma'lumot mavjud emas"),
            "published": item.get("published", ""),
            "link": item.get("link", ""),
            "image": image,
        })

    return news


# ASOSIY
def home(request):

    latest_news = get_news(
        "https://kun.uz/news/rss"
    )

    return render(
        request,
        "news/index.html",
        {
            "latest_news": latest_news
        }
    )


# JAHON
def jahon_news(request):

    news = get_news(
        "https://kun.uz/news/rss"
    )

    return render(
        request,
        "news/category.html",
        {
            "title": "Jahon Yangiliklari",
            "news": news
        }
    )


# SPORT
def sport_news(request):

    news = get_news(
        "https://kun.uz/news/rss"
    )

    return render(
        request,
        "news/category.html",
        {
            "title": "Sport Yangiliklari",
            "news": news
        }
    )


# TEXNOLOGIYA
def texno_news(request):

    news = get_news(
        "https://kun.uz/news/rss"
    )

    return render(
        request,
        "news/category.html",
        {
            "title": "Texnologiya Yangiliklari",
            "news": news
        }
    )


# TALIM
def talim_news(request):

    news = get_news(
        "https://kun.uz/news/rss"
    )

    return render(
        request,
        "news/category.html",
        {
            "title": "Ta'lim Yangiliklari",
            "news": news
        }
    )


# DETAIL
def news_detail(request):

    context = {

        "title": request.GET.get("title"),

        "description": request.GET.get("description"),

        "published": request.GET.get("published"),

        "image": request.GET.get("image"),

        "link": request.GET.get("link"),

        "related_news": get_news(
            "https://kun.uz/news/rss"
        )[:6]

    }

    return render(
        request,
        "news/detail.html",
        context
    )