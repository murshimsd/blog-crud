# Generated by Django 4.1.5 on 2023-06-01 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_blog_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
    ]
