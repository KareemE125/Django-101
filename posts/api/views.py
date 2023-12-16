from rest_framework.decorators import api_view
from rest_framework.response import Response


from ..models import Post
from .serializers import PostSerializer
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/posts',
        'GET /api/posts/:id',
    ]
    
    return Response({"api_routes": routes})

@api_view(['GET'])
def getPosts(requests):
    posts = PostSerializer(Post.objects.all().order_by("id"), many=True)
    json = { "posts_count": len(posts.data), "posts": posts.data }
    
    return Response(json)

@api_view(['GET'])
def getPost(request, id):
    try:
        post = PostSerializer(Post.objects.get(id=id))
        return Response({"post": post.data})
    
    except ObjectDoesNotExist:
        return Response({
            "error":"404 NOT FOUND",
            "Message": f"Post with ID:{id} is Not Found"
        })