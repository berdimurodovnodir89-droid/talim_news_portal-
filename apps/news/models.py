from django.db import models


class RSSSource(models.Model):
    CATEGORY_CHOICES = (
        ("asosiy", "Asosiy"),
        ("texnologiya", "Texnologiya"),
        ("talim", "Talim"),
        ("sport", "Sport"),
        ("jahon", "Jahon"),
    )

    name = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    category_hint = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="asosiy"
    )

    is_active = models.BooleanField(default=True)

    last_fetched = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class NewsItem(models.Model):

    title = models.CharField(max_length=500)

    link = models.URLField(
        unique=True
    )

    summary = models.TextField(
        blank=True
    )

    pub_date = models.DateTimeField()

    image_url = models.URLField(
        blank=True
    )

    source = models.CharField(
        max_length=100
    )

    category = models.CharField(
        max_length=50
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title