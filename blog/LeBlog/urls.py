from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView
#from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-details"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('post/edit/<int:pk>',UpdatePostView.as_view(), name="update_post"),
]