import feedparser
from django.shortcuts import render

import feedparser
def get_category_image(category):

    images = {
        "sport": [
            "https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800",
            "https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=800",
            "https://images.unsplash.com/photo-1517649763962-0c623066013b?w=800",
        ],

        "talim": [
            "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=800",
            "https://images.unsplash.com/photo-1509062522246-3755977927d7?w=800",
            "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800",
        ],

        "texno": [
            "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800",
            "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800",
            "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800",
        ],

        "jahon": [
            "https://images.unsplash.com/photo-1521295121783-8a321d551ad2?w=800",
            "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?w=800",
            "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800",
        ],

        "home": [
            "https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=800",
            "https://images.unsplash.com/photo-1495020689067-958852a7765e?w=800",
            "https://images.unsplash.com/photo-1585829365295-ab7cd400c167?w=800",
        ]
    }

    import random
    return random.choice(images.get(category, images["home"]))

feed = feedparser.parse("https://kun.uz/news/rss")
SPORT_IMAGES = [
    "https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=800",
    "https://images.unsplash.com/photo-1517649763962-0c623066013b?w=800",
    "https://images.unsplash.com/photo-1508098682722-e99c643e7485?w=800",
    "https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800",
    "https://images.unsplash.com/photo-1546519638-68e109498ffc?w=800",
]
TECH_IMAGE = "https://images.unsplash.com/photo-1518770660439-4636190af475"
EDU_IMAGE = "https://images.unsplash.com/photo-1522202176988-66273c2fd55f"
WORLD_IMAGE = "https://images.unsplash.com/photo-1521295121783-8a321d551ad2"
DEFAULT_IMAGE = "https://images.unsplash.com/photo-1504711434969-e33886168f5c"
print(feed.entries[0].keys())
def get_sport_image(title):

    title = title.lower()

    if "ronaldo" in title:
        return "https://images.unsplash.com/photo-1579952363873-27d3bfad9c0d?w=800"

    if "messi" in title:
        return "https://images.unsplash.com/photo-1517466787929-bc90951d0974?w=800"

    if "futbol" in title:
        return "https://images.unsplash.com/photo-1574629810360-7efbbe195018?w=800"

    if "tennis" in title:
        return "https://images.unsplash.com/photo-1622279457486-62dcc4a431d6?w=800"

    if "boks" in title:
        return "https://images.unsplash.com/photo-1549719386-74dfcbf7dbed?w=800"

    return "https://images.unsplash.com/photo-1547347298-4074fc3086f0?w=800"
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

def filter_news(keyword_list, category):

    all_news = get_news()

    filtered = []

    for item in all_news:

        title = item.get("title", "").lower()
        description = item.get("summary", "").lower()

        text = title + " " + description

        for keyword in keyword_list:

            if keyword in text:

                filtered.append({
                    "title": item.get("title"),
                    "description": item.get("summary"),
                    "published": item.get("published"),
                    "link": item.get("link"),
                    "image": get_category_image(category)
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