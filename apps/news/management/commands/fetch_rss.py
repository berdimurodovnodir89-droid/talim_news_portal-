import feedparser
from bs4 import BeautifulSoup

from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.news.models import RSSSource
from apps.news.models import NewsItem


CATEGORY_KEYWORDS = {
    "texnologiya": [
        "iphone",
        "android",
        "ai",
        "robot",
        "google",
        "apple",
        "microsoft",
        "technology",
        "software",
        "computer",
    ],
    "talim": [
        "education",
        "student",
        "university",
        "school",
        "teacher",
        "learning",
    ],
    "sport": [
        "football",
        "soccer",
        "basketball",
        "tennis",
        "olympic",
        "sport",
    ],
    "jahon": [
        "world",
        "war",
        "president",
        "government",
        "russia",
        "china",
        "usa",
    ],
}

CATEGORY_IMAGES = {
    "sport": "https://images.unsplash.com/photo-1517649763962-0c623066013b?w=800",
    "texnologiya": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800",
    "talim": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=800",
    "jahon": "https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?w=800",
    "asosiy": "https://picsum.photos/800/500",
}

def detect_category(title, summary):

    text = f"{title} {summary}".lower()

    for category, keywords in CATEGORY_KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:
                return category

    return "asosiy"

def extract_image(entry):

    try:
        if hasattr(entry, "media_content"):
            return entry.media_content[0]["url"]
    except:
        pass

    try:
        summary = getattr(entry, "summary", "")
        soup = BeautifulSoup(summary, "html.parser")

        img = soup.find("img")

        if img:
            return img.get("src", "")
    except:
        pass

    return ""


class Command(BaseCommand):

    help = "Fetch news from RSS feeds"

    def handle(self, *args, **kwargs):

        sources = RSSSource.objects.filter(
            is_active=True
        )

        if not sources.exists():
            self.stdout.write(
                self.style.WARNING(
                    "No active RSS sources found."
                )
            )
            return

        for source in sources:

            self.stdout.write(
                f"Fetching: {source.name}"
            )

            try:

                feed = feedparser.parse(
                    source.url
                )
                print("ENTRIES:", len(feed.entries))

                for entry in feed.entries:

                    title = getattr(
                        entry,
                        "title",
                        ""
                    )

                    link = getattr(
                        entry,
                        "link",
                        ""
                    )

                    summary = getattr(
                        entry,
                        "summary",
                        ""
                    )
                    image_url = extract_image(entry)

                    if not image_url:
                        image_url = CATEGORY_IMAGES.get(
                            source.category_hint,
                            CATEGORY_IMAGES["asosiy"]
                        )

                    if not link:
                        continue

                    if NewsItem.objects.filter(
                        link=link
                    ).exists():
                        continue

                    try:

                        pub_date = datetime(
                            *entry.published_parsed[:6]
                        )

                    except Exception:

                        pub_date = timezone.now()

                    category = detect_category(
                        title,
                        summary
                    )

                    image_url = CATEGORY_IMAGES.get(
                        category,
                        CATEGORY_IMAGES["asosiy"]
                    )

                    NewsItem.objects.create(
                        title=title,
                        link=link,
                        summary=summary,
                        pub_date=pub_date,
                        source=source.name,
                        category=category,
                        image_url=image_url
                    )

                source.last_fetched = timezone.now()
                source.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Done: {source.name}"
                    )
                )

            except Exception as e:

                self.stdout.write(
                    self.style.ERROR(
                        str(e)
                    )
                )