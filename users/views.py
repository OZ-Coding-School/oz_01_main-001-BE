from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def login_view(request):
    error = None
    if request.user.is_authenticated:
        return redirect('/fridge/fridge_main/')

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/fridge/fridge_main/')
        else:
            error = "Invalid username or password"

    return render(request, 'users/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('/users/login/')

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        vegetarian = request.POST.get("vegetarian", False)
        if username and email and password:
            user = User.objects.create_user(username=username, email=email, password=password, vegetarian=vegetarian)
            if vegetarian:
                user.vegetarian = True
                user.save()
            return redirect('/users/login/')
    return render(request, "users/signup.html")

