
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


RSS_URL = "https://kun.uz/news/rss"


def get_news():

    feed = feedparser.parse(RSS_URL)

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


def filter_news(keywords, images):

    news = get_news()

    results = []

    for item in news:

        text = (
            item["title"] + " " +
            item["description"]
        ).lower()

        if any(word in text for word in keywords):

            item["image"] = random.choice(images)

            results.append(item)

    return results


def home(request):

    latest_news = get_news()

    return render(
        request,
        "news/index.html",
        {
            "latest_news": latest_news
        }
    )


def sport_news(request):

    news = filter_news(
        [
            "sport",
            "futbol",
            "ronaldo",
            "messi",
            "tennis",
            "nba",
            "boks",
            "chempion",
            "gol"
        ],
        SPORT_IMAGES
    )

    return render(
        request,
        "news/category.html",
        {
            "title": "Sport Yangiliklari",
            "news": news
        }
    )


def talim_news(request):

    news = filter_news(
        [
            "ta'lim",
            "maktab",
            "universitet",
            "talaba",
            "imtihon",
            "o‘qituvchi",
            "abituriyent"
        ],
        EDU_IMAGES
    )

    return render(
        request,
        "news/category.html",
        {
            "title": "Ta'lim Yangiliklari",
            "news": news
        }
    )


def texno_news(request):

    news = filter_news(
        [
            "texnologiya",
            "ai",
            "sun'iy intellekt",
            "google",
            "apple",
            "microsoft",
            "robot",
            "internet",
            "it"
        ],
        TECH_IMAGES
    )

    return render(
        request,
        "news/category.html",
        {
            "title": "Texnologiya Yangiliklari",
            "news": news
        }
    )


def jahon_news(request):

    news = filter_news(
        [
            "rossiya",
            "ukraina",
            "tramp",
            "putin",
            "xitoy",
            "aqsh",
            "yevropa",
            "bmt",
            "urush"
        ],
        WORLD_IMAGES
    )

    return render(
        request,
        "news/category.html",
        {
            "title": "Jahon Yangiliklari",
            "news": news
        }
    )


def news_detail(request):

    related_news = random.sample(
        get_news(),
        min(6, len(get_news()))
    )

    context = {
        "title": request.GET.get("title"),
        "description": request.GET.get("description"),
        "published": request.GET.get("published"),
        "image": request.GET.get("image"),
        "link": request.GET.get("link"),
        "related_news": related_news,
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

    query = request.GET.get(
        "q",
        ""
    ).lower().strip()

    results = []

    for item in get_news():

        text = (
            item["title"] + " " +
            item["description"]
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