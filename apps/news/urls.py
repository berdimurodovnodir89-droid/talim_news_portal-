from django.urls import path
from .views import (
    home,
    jahon_news,
    sport_news,
    texno_news,
    talim_news,
    news_detail,
    about,
    search,
)

urlpatterns = [
    path('', home, name='home'),
    path('jahon/', jahon_news, name='jahon'),
    path('sport/', sport_news, name='sport'),
    path('texnologiya/', texno_news, name='texnologiya'),
    path('talim/', talim_news, name='talim'),
    path(
    'detail/<int:pk>/',
    news_detail,
    name='news_detail'
),
    path('about/', about, name='about'),
    path('search/', search, name='search'),
]