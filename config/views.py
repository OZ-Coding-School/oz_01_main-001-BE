from django.shortcuts import redirect

def index(request):
    if request.user.is_authenticated:
        return redirect('/fridge/fridge_main/')
    else:
        return redirect('/users/login/')