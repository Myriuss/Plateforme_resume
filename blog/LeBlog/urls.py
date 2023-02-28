from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCatView, CategoryView, CategoryListView
#from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-details"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_cat/', AddCatView.as_view(), name="add_cat"),
    path('post/edit/<int:pk>',UpdatePostView.as_view(), name="update_post"),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name="delete_post"),
    path('categorie/<str:cats>/', CategoryView, name='categorie'),
    path('categories_list', CategoryListView, name='categories_list'),


]