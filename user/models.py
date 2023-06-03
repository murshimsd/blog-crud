from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 30)
    phone = models.BigIntegerField()
    e_mail = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)
    photo = models.ImageField(upload_to='user/')

    class Meta:
        db_table = 'user_tb'


class Blog(models.Model) :
    blogger_name = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=30,default='')
    users_liked = models.ManyToManyField(User, related_name='liked_categories')
    date_column = models.DateField(default=timezone.now)
    
    class Meta:
        db_table = 'blog_tb'