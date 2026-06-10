import feedparser
from django.shortcuts import render


def get_news():

    feed = feedparser.parse(
        "https://kun.uz/news/rss"
    )

    return feed.entries


def filter_news(keyword_list):

    all_news = get_news()

    filtered = []

    for item in all_news:

        title = item.get(
            "title",
            ""
        ).lower()

        description = item.get(
            "summary",
            ""
        ).lower()

        text = title + " " + description

        for keyword in keyword_list:

            if keyword in text:

                filtered.append({

                    "title": item.get("title"),

                    "description": item.get("summary"),

                    "published": item.get("published"),

                    "link": item.get("link"),

                    "image": f"https://picsum.photos/600/400?random={len(filtered)+1}"

                })

                break

    return filtered


# HOME
def home(request):

    latest_news = []

    for item in get_news():

        latest_news.append({

            "title": item.get("title"),

            "description": item.get("summary"),

            "published": item.get("published"),

            "link": item.get("link"),

            "image": f"https://picsum.photos/600/400?random={len(latest_news)+1}"

        })

    return render(
        request,
        "news/index.html",
        {
            "latest_news": latest_news
        }
    )


def sport_news(request):

    news = filter_news([
        "sport", "futbol", "superliga", "chempionlar", "premyer",
        "liga", "ronaldo", "messi", "barselona", "real", "manchester",
        "goal", "gol", "match", "o'yin", "turnir", "bokschi",
        "ufc", "tennis", "nba", "voleybol", "basketbol", "xokkey",
        "formula", "atletika", "suzish", "gimnastika", "kurash",
        "boks", "mushtlashish", "chempionat", "olimpiya", "medal"
    ])

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
    ])

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
    ])

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
    ])

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

            "image": f"https://picsum.photos/600/400?random={len(related_news)+1}"

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