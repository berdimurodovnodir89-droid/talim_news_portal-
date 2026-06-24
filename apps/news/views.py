
import random
import feedparser

from bs4 import BeautifulSoup
from django.shortcuts import render
SPORT_RSS = "https://kun.uz/news/rss?f=sport"
TECH_RSS = "https://kun.uz/news/rss?f=technology"

RSS_URL = "https://kun.uz/news/rss"


def get_image(item):

    try:
        if "media_content" in item:
            return item.media_content[0]["url"]
    except:
        pass

    try:
        if "links" in item:
            for link in item.links:
                if "image" in str(link):
                    return link.href
    except:
        pass

    return "https://picsum.photos/800/500"
def get_news(rss_url=RSS_URL):

    feed = feedparser.parse(rss_url)

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
            "news": get_news(SPORT_RSS)
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
            "news": get_news(TECH_RSS)
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
