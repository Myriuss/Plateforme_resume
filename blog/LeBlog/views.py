from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categorie
from .forms import PostForm, EditPostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect



# listView allows to list a query set to the datebase
# same thing but details of one record
# def home(request):
# return render(request, 'home.html', {})

def LikeView (request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-details', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categorie.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Categorie.objects.all()
    return render(request, 'cat_menu_list.html', {'cat_menu_list': cat_menu_list})

def CategoryView(request, cats):
    categorie_posts = Post.objects.filter(categorie=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.replace('-', ' '), 'categorie_posts': categorie_posts})

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Categorie.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        return context



class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

class AddCatView(CreateView):
    model = Categorie
    template_name = 'add_cat.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
