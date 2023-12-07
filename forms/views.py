from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
# Create your views here.

def index(request):
    
    if(request.method == 'POST'):
        formData = UserForm(request.POST)
        if(formData.is_valid()):
            formData.save()
            return redirect('home')
    
    return render(request, 'forms/index.html', {"userForm": UserForm})