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


def filter_news(keyword_list, category):

    all_news = get_news()
    filtered = []

    for item in all_news:

        text = (
            item["title"] + " " + item["description"]
        ).lower()

        for keyword in keyword_list:

            if keyword.lower() in text:

                if category == "sport":
                    image = random.choice(SPORT_IMAGES)

                elif category == "talim":
                    image = random.choice(EDU_IMAGES)

                elif category == "texno":
                    image = random.choice(TECH_IMAGES)

                else:
                    image = random.choice(WORLD_IMAGES)

                filtered.append({
                    "title": item["title"],
                    "description": item["description"],
                    "published": item["published"],
                    "link": item["link"],
                    "image": image,
                })

                break

    return filtered


def home(request):
    return render(
        request,
        "news/index.html",
        {
            "latest_news": get_news()
        }
    )


def sport_news(request):

    news = filter_news(
        [
            "sport",
            "futbol",
            "ronaldo",
            "messi",
            "gol",
            "tennis",
            "nba",
            "boks"
        ],
        "sport"
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
            "talaba",
            "universitet",
            "maktab",
            "abituriyent",
            "imtihon",
            "grant",
            "stipendiya",
            "student",
            "bakalavr",
            "magistr",
            "o'qituvchi"
        ],
        "talim"
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
            "ai",
            "chatgpt",
            "google",
            "apple",
            "android",
            "iphone",
            "robot",
            "server",
            "cloud",
            "texnolog"
        ],
        "texno"
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
            "aqsh",
            "xitoy",
            "yevropa",
            "prezident",
            "davlat",
            "jahon",
            "xalqaro"
        ],
        "jahon"
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
    return render(request, "news/about.html")


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