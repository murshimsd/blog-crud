from django.urls import path
from . import views

app_name='user'   #for redirection purpose

urlpatterns=[
    path('home',views.home,name='home'),
    path('master',views.master,name='master'),
    path('detail/<int:bid>',views.detail,name='detail'),
    path('add',views.add,name='add'),
    path('logout',views.logout,name='logout'),
    path('user_blogs/<int:uid>',views.user_blogs,name='user_blogs'),
    path('like_blog',views.like_blog,name='like_blog'),
    # path('like_count',views.get_likes_count,name='like_count'),
    path('update_form/<int:bb_id>',views.update_form,name='update_form'),
    path('delete/<int:bbb_id>',views.delete,name='delete')
   
   
    
   
]