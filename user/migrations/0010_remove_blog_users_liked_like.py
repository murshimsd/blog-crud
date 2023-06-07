# Generated by Django 4.1.5 on 2023-06-06 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_blog_like_status_blog_users_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='users_liked',
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'like_tb',
                'unique_together': {('user', 'blog')},
            },
        ),
    ]