import feedparser
import random
from django.shortcuts import render


SPORT_IMAGES = [
    "https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=800",
    "https://images.unsplash.com/photo-1517649763962-0c623066013b?w=800",
    "https://images.unsplash.com/photo-1508098682722-e99c643e7485?w=800",
]

EDU_IMAGES = [
    "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=800",
    "https://images.unsplash.com/photo-1509062522246-3755977927d7?w=800",
    "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800",
]

TECH_IMAGES = [
    "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800",
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800",
    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800",
]

WORLD_IMAGES = [
    "https://images.unsplash.com/photo-1521295121783-8a321d551ad2?w=800",
    "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?w=800",
    "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800",
]


def get_news():
    feed = feedparser.parse("https://kun.uz/news/rss")

    news = []

    for item in feed.entries:
        news.append({
            "title": item.get("title", ""),
            "description": item.get("summary", ""),
            "published": item.get("published", ""),
            "link": item.get("link", ""),
            "image": random.choice(WORLD_IMAGES),
        })

    return news


def filter_news(category):
    news = get_news()

    for item in news:
        if category == "sport":
            item["image"] = random.choice(SPORT_IMAGES)

        elif category == "talim":
            item["image"] = random.choice(EDU_IMAGES)

        elif category == "texno":
            item["image"] = random.choice(TECH_IMAGES)

        else:
            item["image"] = random.choice(WORLD_IMAGES)

    return news


def home(request):
    return render(
        request,
        "news/index.html",
        {
            "latest_news": get_news()
        }
    )


def sport_news(request):
    return render(
        request,
        "news/category.html",
        {
            "title": "Sport Yangiliklari",
            "news": filter_news("sport")
        }
    )


def talim_news(request):
    return render(
        request,
        "news/category.html",
        {
            "title": "Ta'lim Yangiliklari",
            "news": filter_news("talim")
        }
    )


def texno_news(request):
    return render(
        request,
        "news/category.html",
        {
            "title": "Texnologiya Yangiliklari",
            "news": filter_news("texno")
        }
    )


def jahon_news(request):
    return render(
        request,
        "news/category.html",
        {
            "title": "Jahon Yangiliklari",
            "news": filter_news("jahon")
        }
    )


def news_detail(request):

    context = {
        "title": request.GET.get("title"),
        "description": request.GET.get("description"),
        "published": request.GET.get("published"),
        "image": request.GET.get("image"),
        "link": request.GET.get("link"),
    }

    return render(
        request,
        "news/detail.html",
        context
    )


def about(request):
    return render(
        request,
        "news/about.html"
    )


def search(request):

    query = request.GET.get("q", "").strip().lower()

    results = []

    for item in get_news():

        text = (
            item["title"] + " " + item["description"]
        ).lower()

        if query and query in text:
            results.append(item)

    return render(
        request,
        "news/search.html",
        {
            "query": query,
            "results": results
        }
    )