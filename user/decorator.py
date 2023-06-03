from django.shortcuts import redirect

def auth_user(func):
    def wrapper(request, *args, **kwargs):
        if 'user' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('common:home')
           
    return wrapper