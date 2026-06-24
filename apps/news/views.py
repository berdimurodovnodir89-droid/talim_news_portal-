
import random
import feedparser

from bs4 import BeautifulSoup
from django.shortcuts import render


RSS_URL = "https://kun.uz/news/rss"


def get_image(item):

    if "media_content" in item:
        try:
            return item.media_content[0]["url"]
        except:
            pass

    summary = item.get("summary", "")

    soup = BeautifulSoup(summary, "html.parser")

    img = soup.find("img")

    if img and img.get("src"):
        return img["src"]

    return f"https://picsum.photos/800/500?random={random.randint(1,9999)}"


def get_news():

    feed = feedparser.parse(RSS_URL)

    news = []

    for item in feed.entries:

        news.append({
            "title": item.get("title", ""),
            "description": item.get("summary", ""),
            "published": item.get("published", ""),
            "link": item.get("link", ""),
            "image": get_image(item),
        })

    return news


def filter_news(keywords):

    results = []

    for item in get_news():

        text = (
            item["title"] + " " +
            item["description"]
        ).lower()

        if any(keyword.lower() in text for keyword in keywords):
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

    return render(
        request,
        "news/category.html",
        {
            "title": "Sport Yangiliklari",
            "news": filter_news([
                "sport",
                "futbol",
                "ronaldo",
                "messi",
                "gol",
                "tennis",
                "ufc",
                "nba",
                "boks"
            ])
        }
    )


def talim_news(request):

    return render(
        request,
        "news/category.html",
        {
            "title": "Ta'lim Yangiliklari",
            "news": filter_news([
                "ta'lim",
                "maktab",
                "universitet",
                "talaba",
                "abituriyent",
                "imtihon",
                "o'qituvchi"
            ])
        }
    )


def texno_news(request):

    return render(
        request,
        "news/category.html",
        {
            "title": "Texnologiya Yangiliklari",
            "news": filter_news([
                "texnologiya",
                "ai",
                "google",
                "apple",
                "microsoft",
                "robot",
                "internet",
                "it"
            ])
        }
    )


def jahon_news(request):

    return render(
        request,
        "news/category.html",
        {
            "title": "Jahon Yangiliklari",
            "news": filter_news([
                "rossiya",
                "ukraina",
                "putin",
                "tramp",
                "aqsh",
                "xitoy",
                "yevropa",
                "bmt",
                "urush"
            ])
        }
    )


def news_detail(request):

    all_news = get_news()

    related_news = random.sample(
        all_news,
        min(6, len(all_news))
    )

    return render(
        request,
        "news/detail.html",
        {
            "title": request.GET.get("title"),
            "description": request.GET.get("description"),
            "published": request.GET.get("published"),
            "image": request.GET.get("image"),
            "link": request.GET.get("link"),
            "related_news": related_news,
        }
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
    ).strip().lower()

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
