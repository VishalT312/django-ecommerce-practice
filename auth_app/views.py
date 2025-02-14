from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password != confirm_password:
            messages.warning(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        if User.objects.filter(username=email).exists():
            messages.info(request, 'Email is already taken.')
            return render(request, 'signup.html')

        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        messages.success(
            request, 'Account created successfully. Please log in.')

        return redirect('login')

    return render(request, 'signup.html')


def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login Succesfull')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentils')
            return render(request, 'login.html')

    return render(request, 'login.html')


def handlelogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')


