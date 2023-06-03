from django.shortcuts import render , redirect
from user.models import User
from user.models import Blog
# Create your views here.
from django.shortcuts import render
from .decorator import auth_admin

# Create your views here.




def master_page(request):
    return render(request,'v_admin/master_page.html')

@auth_admin
def home(request):
    blogs = Blog.objects.filter(status='pending')
    return render(request,'v_admin/home.html',{"blogs":blogs})
@auth_admin
def bloggers(request):
    user = User.objects.all()
    return render(request,'v_admin/bloggers.html',{"users":user})


@auth_admin
def approve(request,b_id):
    blog = Blog.objects.get(id=b_id)
    return render(request,'v_admin/approve.html',{"blog":blog})
@auth_admin
def approved(request,bid) :
    blog = Blog.objects.get(id=bid)
    blog.status = 'approved'
    blog.save()
    return redirect("v_admin:home")
@auth_admin
def delete(request,b__id) :
    blog = Blog.objects.get(id=b__id)
    blog.delete()
    return redirect("v_admin:home")
@auth_admin
def logout(request) :
    del request.session['admin']
    request.session.flush()
    return redirect('common:home')

@auth_admin
def aa(request,u_id):
    blog = Blog.objects.filter(blogger_name_id=u_id,status = 'approved')
    return render(request,'v_admin/aa.html',{"blogs":blog})





