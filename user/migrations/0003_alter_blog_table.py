# Generated by Django 4.1.5 on 2023-06-01 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_blog'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blog',
            table='blog_tb',
        ),
    ]
