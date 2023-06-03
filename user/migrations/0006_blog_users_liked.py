# Generated by Django 4.1.5 on 2023-06-03 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_blog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='users_liked',
            field=models.ManyToManyField(related_name='liked_categories', to='user.user'),
        ),
    ]
