from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Categorie(models.Model):
        name = models.CharField(max_length=255)

        def __str__(self):
            return self.name

        def get_absolute_url(self):
                #return reverse('post-details', args=(str(self.id)))
                return reverse('home')

class Profile(models.Model):
        user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
        bio = models.TextField()
        profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

        microsoft_teams_url = models.CharField(max_length=255, null=True, blank=True)
        github_url = models.CharField(max_length=255, null=True, blank=True)
        linkedin_url = models.CharField(max_length=255, null=True, blank=True)

        def __str__(self):
            return str(self.user)

class Post(models.Model):
        title = models.CharField(max_length=255)
        header_image = models.ImageField(null=True, blank=True, upload_to="images/")
        title_tag = models.CharField(max_length=255)
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        body = RichTextField(blank=True, null=True)
        #body = models.TextField()
        post_date = models.DateField(auto_now_add=True)
        categorie = models.CharField(max_length=255)
        snippet = models.CharField(max_length=255, default='coding')
        likes = models.ManyToManyField(User, related_name='resumee')

        def total_likes(self):
                return self.likes.count()

        def __str__(self):
            return self.title + ' | ' + str(self.author)

        def get_absolute_url(self):
                #return reverse('post-details', args=(str(self.id)))
                return reverse('home')

def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Categorie, self).save(*args, **kwargs)