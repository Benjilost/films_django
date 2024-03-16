from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from .forms import *
from .models import *

class MovieListView(ListView):
    model = Movie
    template_name = 'films/index.html'
    context_object_name = 'movies'
    paginate_by = 8

    def get_queryset(self):
        movies_list = Movie.objects.all()
        return movies_list



def single_film(request, film_slug):
    film = get_object_or_404(Movie, slug=film_slug)
    comments = film.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = film
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()

    context = {'film': film, 'comments': comments, 'comment_form': comment_form}

    return render(request, 'films/single_film.html', context )


def categories(request):
    cats = Category.objects.all()
    return render(request, 'films/categories.html', {'cats': cats})


def category_movies(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    movies = Movie.objects.filter(cat=category)
    context = {'category': category, 'movies': movies}
    return render(request, 'films/category_movies.html', context)


def add_film(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm()
    return render(request, 'films/add_film.html', {'form': form})


class CommentDeleteView(DeleteView):
    model = MovieComment
    template_name = 'films/comment_confirm_delete.html'

    def get_success_url(self):
        movie = self.object.movie
        return reverse_lazy('single_film', kwargs={'film_slug': movie.slug})

    # def get_queryset(self):
    #     # Возвращает только те комментарии, которые принадлежат текущему пользователю
    #     return MovieComment.objects.filter(user=self.request.user)

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'films/register.html'
    success_url = reverse_lazy('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'films/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')



