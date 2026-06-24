import feedparser
from django.shortcuts import render


RSS_URL = "https://kun.uz/news/rss"


def get_news():
    feed = feedparser.parse(RSS_URL)

    news = []

    for item in feed.entries:

        image = "https://picsum.photos/800/500"

        try:
            if "media_content" in item:
                image = item.media_content[0]["url"]
        except:
            pass

        news.append({
            "title": item.get("title", ""),
            "description": item.get("summary", ""),
            "published": item.get("published", ""),
            "link": item.get("link", ""),
            "image": image,
        })

    return news


def filter_news(keywords):

    results = []

    for item in get_news():

        text = (
            item["title"] + " " + item["description"]
        ).lower()

        if any(word.lower() in text for word in keywords):
            results.append(item)

    return results


def home(request):

    return render(
        request,
        "news/index.html",
        {
            "latest_news": get_news()
        }
    )


def sport_news(request):

    news = filter_news([
        "sport",
        "futbol",
        "messi",
        "ronaldo",
        "gol",
        "tennis",
        "nba",
        "boks",
        "chempionat",
        "jch"
    ])

    return render(
        request,
        "news/category.html",
        {
            "title": "Sport Yangiliklari",
            "news": news
        }
    )


def talim_news(request):

    news = filter_news([
        "ta'lim",
        "universitet",
        "maktab",
        "imtihon",
        "abituriyent",
        "talaba",
        "student",
        "o'qituvchi",
        "magistr",
        "bakalavr"
    ])

    return render(
        request,
        "news/category.html",
        {
            "title": "Ta'lim Yangiliklari",
            "news": news
        }
    )


def texno_news(request):

    news = filter_news([
        "texnologiya",
        "ai",
        "sun'iy intellekt",
        "robot",
        "internet",
        "google",
        "apple",
        "microsoft",
        "tesla",
        "it",
        "chatgpt",
        "openai"
    ])

    return render(
        request,
        "news/category.html",
        {
            "title": "Texnologiya Yangiliklari",
            "news": news
        }
    )


def jahon_news(request):

    news = filter_news([
        "rossiya",
        "ukraina",
        "amerika",
        "aqsh",
        "xitoy",
        "yevropa",
        "putin",
        "trump",
        "bmt",
        "nato",
        "isroil",
        "eron",
        "turkiya"
    ])

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

    return render(
        request,
        "news/about.html"
    )


def search(request):

    query = request.GET.get("q", "").strip().lower()

    results = []

    if query:

        for item in get_news():

            title = item["title"].lower()
            description = item["description"].lower()

            if (
                query in title or
                query in description
            ):
                results.append(item)

    return render(
        request,
        "news/search.html",
        {
            "query": query,
            "results": results
        }
    )