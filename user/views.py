from django.http import JsonResponse
from django.shortcuts import render,redirect
from user.models import Blog
from .decorator import auth_user
from .models import User



# Create your views here.
@auth_user
def home(request):
    blogs = Blog.objects.filter(status="approved")
    return render(request,'user/home.html',{"blogs":blogs})



def user_blogs(request,uid) :
    blogs = Blog.objects.filter(blogger_name_id = uid,status = 'approved')
    return render(request,'user/user_blogs.html',{"blogs":blogs})



@auth_user
def master(request):
    return render(request,'user/master.html')

@auth_user
def detail(request,bid):
    blogs = Blog.objects.get(id=bid)
    return render(request,'user/detail.html',{"blogs":blogs})


@auth_user
def add(request):
    msg = ''
    users = User.objects.get(id=request.session['user'])
    if request.method == 'POST':
        b_title = request.POST['title']
        b_content = request.POST['content']

        new_user = Blog(
            title = b_title,
            content = b_content,
            blogger_name_id = request.session["user"],
            status = 'pending'
        )
        new_user.save()
        msg = 'success'
        
    
    return render(request,'user/add.html',{"user":users,"msgs":msg})


@auth_user
def logout(request) :
    del request.session['user']
    request.session.flush()
    return redirect('common:home')



@auth_user
def update_form(request,bb_id):
    msg = ''
    blog = Blog.objects.get(id=bb_id)
    if request.method == 'POST':
        n_title = request.POST['title']
        n_content = request.POST['content']

        blog.title = n_title
        blog.content = n_content
        blog.save()
        msg = 'success'
    return render(request,'user/update_form.html',{"blog":blog,"msg":msg})




@auth_user
def delete(request,bbb_id):
    blog = Blog.objects.get(id=bbb_id)
    blog.delete()
    return redirect('user:home')






    
@auth_user
def like_blog(request):
    if request.method == 'POST':
        blog_id = int(request.POST.get('blog_id'))
        
        # Assuming you have a Blog model with a 'likes' field and a ManyToManyField for users who liked the blog
        blog = Blog.objects.get(id=blog_id)
        
        # Get the currently logged-in user (assuming you have implemented user authentication)
        user = request.user
        
        if user in blog.users_liked.all():
            # User has already liked the blog, return the current like count
            return JsonResponse({'like_count': blog.likes})
        
        # User has not liked the blog before, increment the like count and add the user to the liked users list
        blog.likes += 1
        blog.users_liked.add(user)
        blog.save()

        return JsonResponse({'like_count': blog.likes})

        