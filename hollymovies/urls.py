from django.contrib import admin
from django.urls import path

from viewer.views import (
    CreatorsListView,
    CreatorView,
    GenresListView,
    GenresTemplateView,
    GenresView,
    countries,
    genre,
    genres,
    home,
    movie,
    movies,
    one_country,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("movies/", movies, name="movies"),
    path("movie/<int:pk>/", movie, name="movie"),
    # path('genres/', genres, name='genres'),  # view pomocí funkce genres
    # path('genres/', GenresView.as_view(), name='genres'),  # view pomocí třídy GenresView
    # path('genres/', GenresTemplateView.as_view(), name='genres'),  # view pomocí třídy GenresTemplateView
    path(
        "genres/", GenresListView.as_view(), name="genres"
    ),  # view pomocí třídy GenresListView
    path("genre/<int:pk>/", genre, name="genre"),
    path("creators/", CreatorsListView.as_view(), name="creators"),
    path("creator/<int:pk>/", CreatorView.as_view(), name="creator"),
    path("countries/", countries, name="country_list"),
    path("country/<int:pk>/", one_country, name="one_country"),
]
