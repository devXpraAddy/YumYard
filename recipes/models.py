from django.db import models
from django.contrib.auth.models import User

class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    youtube_url = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    def youtube_embed_url(self):
        # configurations for proper embedding of youtube videos
        if self.youtube_url:
            if 'watch' in self.youtube_url:
                if '&' in self.youtube_url:
                    temp = self.youtube_url.split('=')[-2].split('&')[0]
                else:
                    temp = self.youtube_url.split('=')[-1]
            else:
                temp = self.youtube_url.split('/')[-1]
            
            return f'https://www.youtube.com/embed/{temp}'
        return None
    

    def __str__(self):
        return self.name
