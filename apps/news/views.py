
import random
import feedparser

from bs4 import BeautifulSoup
from django.shortcuts import render

RSS_URL = "https://kun.uz/news/rss"
SPORT_RSS = "https://kun.uz/news/rss?f=sport"
TECH_RSS = "https://kun.uz/news/rss?f=technology"


SPORT_IMAGES = [
    "https://images.unsplash.com/photo-1517649763962-0c623066013b?w=800",
    "https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=800",
    "https://images.unsplash.com/photo-1508098682722-e99c643e7485?w=800",
]

TECH_IMAGES = [
    "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800",
    "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800",
    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800",
]

EDU_IMAGES = [
    "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=800",
    "https://images.unsplash.com/photo-1509062522246-3755977927d7?w=800",
    "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800",
]

WORLD_IMAGES = [
    "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?w=800",
    "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800",
    "https://images.unsplash.com/photo-1521295121783-8a321d551ad2?w=800",
]


def get_image(item):

    try:
        if "media_content" in item:
            return item.media_content[0]["url"]
    except:
        pass

    try:
        summary = item.get("summary", "")
        soup = BeautifulSoup(summary, "html.parser")
        img = soup.find("img")

        if img and img.get("src"):
            return img["src"]
    except:
        pass

    return f"https://picsum.photos/800/500?random={random.randint(1,999999)}"


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


def set_category_images(news, images):

    for item in news:
        item["image"] = random.choice(images)

    return news


def filter_news(keywords):

    results = []

    for item in get_news():

        text = (
            item["title"] + " " +
            item["description"]
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

    news = get_news(SPORT_RSS)
    news = set_category_images(news, SPORT_IMAGES)

    return render(
        request,
        "news/category.html",
        {
            "title": "Sport Yangiliklari",
            "news": news
        }
    )


def talim_news(request):

    news = get_news()[:20]
    news = set_category_images(news, EDU_IMAGES)

    return render(
        request,
        "news/category.html",
        {
            "title": "Ta'lim Yangiliklari",
            "news": news
        }
    )


def texno_news(request):

    news = get_news(TECH_RSS)
    news = set_category_images(news, TECH_IMAGES)

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
        "putin",
        "tramp",
        "aqsh",
        "xitoy",
        "yevropa",
        "bmt",
        "urush",
        "eron",
        "isroil"
    ])

    if not news:
        news = get_news()[:20]

    news = set_category_images(news, WORLD_IMAGES)

    return render(
        request,
        "news/category.html",
        {
            "title": "Jahon Yangiliklari",
            "news": news
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

    query = request.GET.get("q", "").strip().lower()

    results = []

    if query:

        for item in get_news():

            text = (
                item["title"] + " " +
                item["description"]
            ).lower()

            if query in text:
                results.append(item)

    return render(
        request,
        "news/search.html",
        {
            "query": query,
            "results": results
        }
    )
