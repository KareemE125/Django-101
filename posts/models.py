from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']
        

class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name 
        
        
class Post(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    images = models.ImageField(upload_to='files/posts/images/%y/%m/%d', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    isDeleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
    