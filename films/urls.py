
from django.urls import path
from films.views import *

urlpatterns = [
    path('films/', FilmListCreateView.as_view(), name='film-list-create'),
    path('films/<int:pk>/', FilmDetailView.as_view(), name='film-detail'),
    path('like/<int:film_id>/', toggle_like, name='toggle_like'),
    path('genre/',GenreFilmList.as_view()),
    path('year/',YearFilmList.as_view()),
    path('tags/',TagsFilmList.as_view()),

]