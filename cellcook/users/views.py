from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User

def signup(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        email = request.POST.get('email')  # email is optional
        user = User.objects.create_user(id=id, password=password, email=email)
        return redirect('login')
    else:
        return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        user = authenticate(request, id=id, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'login', {'error': 'Invalid login'})
    else:
        return render(request, 'login.html')
