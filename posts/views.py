from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')

def post(request, id):
    return render(request, 'posts/post.html', {'post': Post.objects.get(id=id)} )

def addPost(request):
    postData = PostForm()
    if request.method == 'POST':
        postData = PostForm(request.POST, request.FILES)
        if postData.is_valid(): 
            postData.save()
            return redirect('posts')

    return render(request, 'posts/editPost.html', {'postForm': postData} )

def editPost(request, id):
    post = Post.objects.get(id=id)
    postData = PostForm(instance=post)
    
    if request.method == 'POST':
        postData = PostForm(request.POST, request.FILES, instance=post)
        if postData.is_valid(): 
            postData.save()
            return redirect('posts')
        
    return render(request, 'posts/editPost.html', {'id': id, 'postForm': postData} )

def deletePost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request, 'posts/deletePost.html', {"post": post})


def postsList(request):
    return render(request, 'posts/postsList.html', {'posts': Post.objects.all()})