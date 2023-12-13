from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def default(request):
    return redirect('login')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    
    return render(request, 'authentication/login.html',{"title": "Login"})

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
    
        return redirect('login')
    
    return render(request, 'authentication/login.html', {"title": "Register"})

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def userProfile(request, id):
    user = request.user
    posts = user.posts.all()
    postsCount = posts.count()
    context = {
        'user': user,
        'posts': posts,
        'postsCount': postsCount,
    }
    return render(request, 'authentication/userProfile.html', context)
