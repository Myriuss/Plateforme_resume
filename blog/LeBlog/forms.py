from django import forms
from django.contrib.auth.models import User
from .models import Post, Categorie, Profile, Comment
from django.contrib.auth.forms import UserChangeForm

choices = [('Analyse financière', 'Analyse financière'),
           ('Analyse des données', 'Analyse des données'),
           ('Réseau', 'Réseau'),
           ('Compilation', 'Compilation'),
           ('programmation linéaire', 'programmation linéaire'),
           ('droit des affaires', 'droit des affaires'),
           ('django python', 'django python'),
           ('php', 'php'),
           ('Conception Orientée objet', 'Conception Orientée objet'),
           ('Programmation Web', 'Programmation Web'),
           ('SQL Server', 'SQL Server'),
           ('Programmation orientée object', 'Programmation orientée object'),
           ('C++', 'C++'),
           ]
choices = Categorie.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class CreateProfilePageForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    microsoft_teams_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    github_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    linkedin_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('bio', 'microsoft_teams_url', 'github_url', 'linkedin_url')

class EditProfilePageForm(UserChangeForm):
    #bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    #microsoft_teams_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #github_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #linkedin_url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ('bio', 'microsoft_teams_url', 'github_url', 'linkedin_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'microsoft_teams_url': forms.TextInput(attrs={'class': 'form-control'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'categorie', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'categorie': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            #'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }