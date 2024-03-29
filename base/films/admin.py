from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
