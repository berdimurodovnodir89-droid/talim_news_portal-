from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'sport/',
        views.sport_news,
        name='sport_news'
    ),

    path(
        'talim/',
        views.talim_news,
        name='talim_news'
    ),

    path(
        'texnologiya/',
        views.texno_news,
        name='texno_news'
    ),

    path(
        'jahon/',
        views.jahon_news,
        name='jahon_news'
    ),

    path(
        'detail/',
        views.news_detail,
        name='news_detail'
    ),

]