from django.shortcuts import render
from .models import User
# Create your views here.

def index(request):
    body = request.POST.dict()
    username = body.get('username', '')
    password = body.get('password', '')
    
    if username and password:
        User(username=username, password=password).save()
    
    return render(request, 'forms/index.html')