from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
 
app_name='common'   #for redirection purpose

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('master',views.master,name='master'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('check_mail',views.check_mail,name='check_mail')

    
   
]