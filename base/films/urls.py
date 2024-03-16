from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('',  MovieListView.as_view(), name='home'),
    path('single_film/<slug:film_slug>', single_film, name='single_film'),
    path('categories/', categories, name='categories'),
    path('categories/<slug:category_slug>', category_movies, name='category_movies'),
    path('add_film/', add_film, name='add_film'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]
