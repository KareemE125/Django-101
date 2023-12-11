from django.shortcuts import render, redirect
from .models import Post, Author, Category
from .forms import PostForm

# Create your views here.
def postsList(request):
    bc = request.GET.get("bc")
    ba = request.GET.get("ba")
    
    posts = Post.objects.all()
    
    if bc and bc!= "all":
        posts = posts.filter(category__name = bc)
    
    if ba and ba!= "all":
        posts = posts.filter(author__name = ba)

    context = {
        'posts': posts, 
        'authors': Author.objects.all(),
        'categories': Category.objects.all(),
    }
    
    return render(request, 'posts/postsList.html', context)


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


