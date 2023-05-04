from django.contrib import admin
from .models import Post, Categorie, Profile, Comment

admin.site.register(Post)
admin.site.register(Categorie)
admin.site.register(Profile)
admin.site.register(Comment)