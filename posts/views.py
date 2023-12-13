from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from django.contrib.auth.models import User
from .forms import PostForm

# Create your views here.
@login_required(login_url='/auth/login')
def postsPage(request):
    bc = request.GET.get("bc")
    ba = request.GET.get("ba")
    search = request.GET.get("search")
    
    posts = Post.objects.all()
    
    if 'reset' in request.GET:
        return redirect('posts')
    
    if search:
        posts = posts.filter(
            Q(title__icontains = search) | 
            Q(content__icontains = search) |
            Q(author__username__icontains = search) |
            Q(category__name__icontains = search)
        )
        
    if bc and bc!= "all":
        posts = posts.filter(category__name = bc)
    
    if ba and ba!= "all":
        posts = posts.filter(author__username = ba)

    context = {
        'posts': posts,
        'postCount': posts.count(),
        'authors': User.objects.filter(posts__isnull=False).distinct(),
        'categories': Category.objects.all(),
    }
    
    return render(request, 'posts/postsPage.html', context)

@login_required(login_url='/auth/login')
def postPage(request, id):
    return render(request, 'posts/postPage.html', {'post': Post.objects.get(id=id)} )

@login_required(login_url='/auth/login')
def addPost(request):
    postData = PostForm()
    if request.method == 'POST':
        postData = PostForm(request.POST, request.FILES)
        if postData.is_valid(): 
            postData.save()
            return redirect('posts')

    return render(request, 'posts/editPost.html', {'postForm': postData} )

@login_required(login_url='/auth/login')
def editPost(request, id):
    post = Post.objects.get(id=id)
    postData = PostForm(instance=post)
    
    if request.method == 'POST':
        postData = PostForm(request.POST, request.FILES, instance=post)
        if postData.is_valid(): 
            postData.save()
            return redirect('posts')
        
    return render(request, 'posts/editPost.html', {'id': id, 'postForm': postData} )

@login_required(login_url='/auth/login')
def deletePost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request, 'posts/deletePost.html', {"post": post})


