from django.contrib import admin

from .models import NewsItem
from .models import RSSSource


@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "source",
        "category",
        "pub_date",
        "created_at"
    )

    list_filter = (
        "category",
        "source"
    )

    search_fields = (
        "title",
        "summary"
    )

    ordering = (
        "-pub_date",
    )

    readonly_fields = (
        "created_at",
    )

    list_per_page = 50

@admin.register(RSSSource)
class RSSSourceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "url",
        "is_active",
        "last_fetched",
        "category_hint"
    )

    list_editable = (
        "is_active",
    )

    list_filter = (
        "is_active",
        "category_hint"
    )

    search_fields = (
        "name",
        "url",
    )