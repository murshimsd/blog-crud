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
    date_column = models.DateField(default=timezone.now)
    
    class Meta:
        db_table = 'blog_tb'







class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'blog')
        db_table = 'like_tb'