from django.db import models

# Create your models here.
#define the models here
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    #slug is part of URL and defines the post
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title
    