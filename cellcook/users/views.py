from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email', '')  # email is optional
        is_vegitarian = request.POST.get('vegitarian', False)
        user = User.objects.create_user(username=username, password=password, email=email)
        return redirect('login')
    else:
        return render(request, 'signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('fridge-main')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('fridge')
        else:
            return render(request, 'login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)

    return redirect("/")
