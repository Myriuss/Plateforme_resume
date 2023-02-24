from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
#listView allows to list a query set to the datebase
#same thing but details of one record
#def home(request):
   # return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'