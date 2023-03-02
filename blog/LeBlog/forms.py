from django import forms
from .models import Post, Categorie

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

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'categorie', 'body')

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