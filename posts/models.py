from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']
        
        
        
        
class Post(models.Model):
    categories = [('technology', 'Technology'), ('fashion', 'Fashion'), ('cars', 'Cars'), ('sports', 'Sports'), ('health', 'Health'), ('politics', 'Politics'), ('travel', 'Travel'), ('food', 'Food'), ('music', 'Music'), ('movies', 'Movies'), ('games', 'Games'), ('books', 'Books'), ('art', 'Art'), ('animals', 'Animals'), ('other', 'Other')]
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    images = models.ImageField(upload_to='files/posts/images/%y/%m/%d', null=True, blank=True)
    category = models.CharField(max_length=255, choices=categories, default='other')
    isDeleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
    