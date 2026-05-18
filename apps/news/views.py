import feedparser
from django.shortcuts import render


def get_news_by_keywords(keywords):

    feed = feedparser.parse(
        "https://kun.uz/news/rss"
    )

    items = []

    for item in feed.entries:

        title = item.title.lower()

        summary = ""

        if hasattr(item, "summary"):
            summary = item.summary.lower()

        for keyword in keywords:

            if keyword in title or keyword in summary:

                items.append({
                    'title': item.title,
                    'summary': item.summary,
                    'published': item.published,
                })

                break

    return items


# ASOSIY
def home(request):

    feed = feedparser.parse(
        "https://kun.uz/news/rss"
    )

    items = []

    for item in feed.entries[:12]:

        items.append({
            'title': item.title,
            'summary': item.summary,
            'published': item.published,
        })

    return render(
        request,
        'news/category.html',
        {
            'items': items,
            'page_title': "So‘nggi Yangiliklar",
            'logo': "TA'LIM NEWS"
        }
    )


# SPORT
def sport_news(request):

    feed = feedparser.parse(
        "https://kun.uz/news/rss"
    )

    items = []

    sport_keywords = [
        "sport",
        "futbol",
        "messi",
        "ronaldo",
        "chempion",
        "liga",
        "gol",
        "o‘yin",
        "stadion",
        "turnir",
        "ufc",
        "boks",
        "osiyo",
        "kubok",
        "terma",
    ]

    for item in feed.entries:

        title = item.title.lower()

        summary = ""

        if hasattr(item, "summary"):
            summary = item.summary.lower()

        if any(
            word in title or word in summary
            for word in sport_keywords
        ):

            items.append({
                'title': item.title,
                'summary': item.summary,
                'published': item.published,
            })

    # AGAR SPORT TOPILMASA
    if len(items) == 0:

        for item in feed.entries[:12]:

            items.append({
                'title': item.title,
                'summary': item.summary,
                'published': item.published,
            })

    return render(
        request,
        'news/category.html',
        {
            'items': items,
            'page_title': "Sport Yangiliklari",
            'logo': "SPORT NEWS"
        }
    )

# TA'LIM
def talim_news(request):

    keywords = [
        "ta'lim",
        "maktab",
        "universitet",
        "talaba",
        "abituriyent",
        "imtihon",
        "o‘qituvchi",
        "dars",
    ]

    items = get_news_by_keywords(
        keywords
    )

    return render(
        request,
        'news/category.html',
        {
            'items': items,
            'page_title': "Ta'lim Yangiliklari",
            'logo': "TA'LIM NEWS"
        }
    )


# TEXNOLOGIYA
def texno_news(request):

    keywords = [
        "texnologiya",
        "ai",
        "sun’iy intellekt",
        "google",
        "iphone",
        "samsung",
        "robot",
        "internet",
        "it",
        "python",
        "dastur",
    ]

    items = get_news_by_keywords(
        keywords
    )

    return render(
        request,
        'news/category.html',
        {
            'items': items,
            'page_title': "Texnologiya Yangiliklari",
            'logo': "TEXNO NEWS"
        }
    )


# JAHON
def jahon_news(request):

    keywords = [
        "rossiya",
        "amerika",
        "xitoy",
        "ukraina",
        "yevropa",
        "tramp",
        "putin",
        "jahon",
        "urush",
        "turkiya",
    ]

    items = get_news_by_keywords(
        keywords
    )

    return render(
        request,
        'news/category.html',
        {
            'items': items,
            'page_title': "Jahon Yangiliklari",
            'logo': "JAHON NEWS"
        }
    )

def news_detail(request):

    title = request.GET.get('title')
    summary = request.GET.get('summary')
    published = request.GET.get('published')

    return render(
        request,
        'news/detail.html',
        {
            'title': title,
            'summary': summary,
            'published': published,
        }
    )