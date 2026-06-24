import feedparser
from django.shortcuts import render

import feedparser

feed = feedparser.parse("https://kun.uz/news/rss")
SPORT_IMAGE = "https://images.unsplash.com/photo-1547347298-4074fc3086f0"
TECH_IMAGE = "https://images.unsplash.com/photo-1518770660439-4636190af475"
EDU_IMAGE = "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"
WORLD_IMAGE = "https://images.unsplash.com/photo-1521295121783-8a321d551ad2"
DEFAULT_IMAGE = "https://images.unsplash.com/photo-1504711434969-e33886168f5c"
print(feed.entries[0].keys())

def get_news():

    feed = feedparser.parse("https://kun.uz/news/rss")

    news = []

    for item in feed.entries:

        news.append({
            "title": item.get("title", ""),
            "description": item.get("summary", ""),
            "published": item.get("published", ""),
            "link": item.get("link", ""),
            "image": DEFAULT_IMAGE,
        })

    return news

def filter_news(keyword_list, image_url):

    filtered = []

    for item in get_news():

        title = item.get("title", "")
        description = item.get("description", "")

        text = (title + " " + description).lower()

        for keyword in keyword_list:

            if keyword in text:

                filtered.append({
                    "title": title,
                    "description": description,
                    "published": item.get("published", ""),
                    "link": item.get("link", ""),
                    "image": image_url
                })

                break

    return filtered

# HOME
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
    "sport","futbol","ronaldo","messi","gol",
    "match","turnir","ufc","tennis","nba",
    "basketbol","boks","olimpiya"
], SPORT_IMAGE)
    return render(
        request,
        "news/category.html",
        {
            "title": "Sport Yangiliklari",
            "news": news
        }
    )


# JAHON
def jahon_news(request):

    news = filter_news([
        "rossiya", "ukraina", "aqsh", "yevropa", "xitoy",
        "jahon", "putin", "tramp", "fransiya", "germaniya",
        "isroil", "eron", "hindiston", "dunyo", "global",
        "xalqaro", "chet", "tashqi", "davlat", "prezident",
        "hukumat", "urush", "tinchlik", "shartnoma", "ittifoq",
        "bmt", "nato", "diplomatiya", "vazir", "qo'shni",
        "arab", "turk", "britaniya", "yaponiya", "koreya"
    ], WORLD_IMAGE)

    return render(
        request,
        "news/category.html",
        {
            "title": "Jahon Yangiliklari",
            "news": news
        }
    )


# TEXNOLOGIYA
def texno_news(request):

    news = filter_news([
        "iphone", "android", "texnolog", "ai", "sun'iy",
        "robot", "internet", "apple", "google", "microsoft",
        "dastur", "ilm", "fan", "innovatsiya", "raqamli",
        "kompyuter", "gadget", "elektron", "samsung", "huawei",
        "chatgpt", "sun'iy intellekt", "kiberhujum", "xaker",
        "crypto", "bitcoin", "blokcheyn", "startap", "it",
        "cloud", "server", "network"
    ], TECH_IMAGE)

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

    news = filter_news([
        "ta'lim", "maktab", "universitet", "imtihon",
        "student", "abituriyent", "grant", "talaba",
        "o'quvchi", "dtm", "diplom", "ilm", "fan",
        "magistr", "bakalavr", "kollej", "litsey",
        "o'qituvchi", "rektor", "dekan", "kafedra",
        "stipendiya", "kurs", "dars", "sinf", "o'quv",
        "ta'lim vazirligi", "toshkent", "pedagog"
    ], EDU_IMAGE)

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

    related_news = []

    all_news = get_news()

    for item in all_news[:6]:

        related_news.append({

            "title": item.get("title"),

            "description": item.get("summary"),

            "published": item.get("published"),

            "link": item.get("link"),

            "image": item.get("media_content", [{}])[0].get(
                "url",
                "https://via.placeholder.com/600x400"
)

        })

    context = {

        "title": request.GET.get("title"),

        "description": request.GET.get("description"),

        "published": request.GET.get("published"),

        "image": request.GET.get("image"),

        "link": request.GET.get("link"),

        "related_news": related_news

    }

    return render(
        request,
        "news/detail.html",
        context
    )


# ABOUT
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