from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Categorie(models.Model):
        name = models.CharField(max_length=255)

        def __str__(self):
            return self.name

        def get_absolute_url(self):
                #return reverse('post-details', args=(str(self.id)))
                return reverse('home')

class Post(models.Model):
        title = models.CharField(max_length=255)
        title_tag = models.CharField(max_length=255)
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        body = models.TextField()
        post_date = models.DateField(auto_now_add=True)
        categorie = models.CharField(max_length=255)

        def __str__(self):
            return self.title + ' | ' + str(self.author)

        def get_absolute_url(self):
                #return reverse('post-details', args=(str(self.id)))
                return reverse('home')
