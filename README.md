# Plateforme de résumé d'une école

Cette application est une plateforme permettant aux étudiants de publier leurs résumés de cours en ligne. Les utilisateurs peuvent créer un compte, soumettre des résumés de cours et les partager avec d'autres étudiants.

## Configuration requise

- Python 3.x
- Django 3.x
- Pillow 9.5.0
- django-ckeditor 6.5.1
- virtualenv 20.19.0

## Installation

1. Clonez le dépôt du projet sur votre ordinateur
2. Ouvrez un terminal à la racine du dossier cloné
3. Créez un environnement virtuel `python -m venv venv`
4. Activez l'environnement virtuel `source venv/bin/activate` (Linux/MacOS) ou `.\venv\Scripts\activate` (Windows)
5. Installez les dépendances 
6. Migrer la base de données `python manage.py migrate`

## Utilisation

1. Lancez le serveur Django `python manage.py runserver`
2. Accédez à l'application dans votre navigateur en visitant l'URL http://localhost:8000/

## Fonctionnalités

- Création de compte utilisateur
- Soumission de résumés de cours (texte, photo)
- Ajout de nouvelles catégories
- Espace utilisateur


## Auteurs

- Myriuss 
