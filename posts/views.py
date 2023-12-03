from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def post(request):
    return render(request, 'posts/post.html', )

def postsList(request):
    return render(request, 'posts/postsList.html', {'posts': Post.objects.all()})