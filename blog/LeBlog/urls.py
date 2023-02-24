from django.urls import path
from .views import HomeView
#from . import views

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home")
]