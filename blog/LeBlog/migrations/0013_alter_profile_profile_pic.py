# Generated by Django 4.1.7 on 2023-05-04 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeBlog', '0012_remove_profile_microsoft_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='images/profile/'),
        ),
    ]
