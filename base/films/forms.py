from django import forms
from django.contrib.auth.models import User

from .models import *
from django.contrib.auth.forms import UserCreationForm



class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'image', 'release_year', 'cat']

    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}))

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введите описание'}))

    release_year = forms.ChoiceField(
        choices=[(year, year) for year in range(1900, 2025)],
        initial=2000,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'formFile'}))

    cat = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ['comment']

    # person = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}))
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Введите комментарий'}))




