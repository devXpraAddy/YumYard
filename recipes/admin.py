from django.contrib import admin
from .models import Recipes

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'ingredients', 'steps', 'youtube_url', 'image']

admin.site.register(Recipes, RecipeAdmin)