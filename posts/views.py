from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post, Author, Category
from .forms import PostForm

# Create your views here.
@login_required(login_url='/auth/login')
def postsList(request):
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
            Q(author__name__icontains = search) |
            Q(category__name__icontains = search)
        )
        
    if bc and bc!= "all":
        posts = posts.filter(category__name = bc)
    
    if ba and ba!= "all":
        posts = posts.filter(author__name = ba)

    context = {
        'posts': posts,
        'postCount': posts.count(),
        'authors': Author.objects.all(),
        'categories': Category.objects.all(),
    }
    
    return render(request, 'posts/postsList.html', context)

@login_required(login_url='/auth/login')
def post(request, id):
    return render(request, 'posts/post.html', {'post': Post.objects.get(id=id)} )

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


