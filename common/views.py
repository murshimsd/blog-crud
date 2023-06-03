from urllib import request
from django.shortcuts import render ,redirect
from user.models import User
from django.http import JsonResponse

from v_admin.models import Admin

# Create your views here.
def home(request):
    return render(request,'common/home.html')

def login(request):
    msg = ''
    if request.method == 'POST' :
        emails = request.POST['email']
        passwords = request.POST['userId']

        try:
            user = User.objects.get(e_mail = emails , password = passwords)
            request.session['user'] = user.id
            request.session['user_name'] = user.name
            request.session['user_photo'] = user.photo.url
            return redirect('user:home')
            

        except :
            msg = 'incorrect'
    return render(request,'common/login.html',{"msg":msg})


def sign_up(request):
    msg = ''
    if request.method == 'POST':
        u_name = request.POST['name']
        u_email = request.POST['email']
        u_password= request.POST['password']
        u_phone= request.POST['phone']
        u_gender= request.POST['gender']
        u_photo= request.FILES['photo']

        user_exist = User.objects.filter(e_mail = u_email).exists()

        if not user_exist :
            new_user = User(
                name = u_name,
                e_mail = u_email,
                password = u_password,
                phone = u_phone,
                gender =u_gender,
                photo = u_photo
            )
            new_user.save()
            msg = 'successfull'
        else:
            msg = 'email exist'






    return render(request,'common/sign_up.html',{"msg":msg})


def master(request):
    return render(request,'common/master.html')


def admin_login(request):
    msg = ''
    if request.method == 'POST':
        u_name = request.POST['email']
        passwords = request.POST['userId']

        try:
            admins = Admin.objects.get(user_id = u_name,password=passwords)
            request.session['admin'] = admins.id
            msg = 'correct'
            return redirect('v_admin:home')
        except:
            msg = 'incorrect'
    return render(request,'common/admin_login.html',{"msgs":msg})

def check_mail(request):
    email_ajax = request.POST['userEmail'] #recieved from ajax
    exist = User.objects.filter(e_mail=email_ajax).exists()
    return JsonResponse({"email_exist":exist})

