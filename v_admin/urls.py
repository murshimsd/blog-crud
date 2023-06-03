from django.urls import path
from . import views
 
app_name='v_admin'   #for redirection purpose

urlpatterns=[
  
    path('master_page',views.master_page,name='master_page'),
    path('home',views.home,name='home'),
    path('bloggers',views.bloggers,name='bloggers'),
    
    path('approve/<int:b_id>',views.approve,name='approve'),
    path('approved/<int:bid>',views.approved,name='approved'),
    path('delete/<int:b__id>',views.delete,name='delete'),
    path('logout',views.logout,name='logout'),
    path('aa/<int:u_id>',views.aa,name='aa')



    
   
]