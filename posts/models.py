from django.conf import settings
from django.db import models

class Post(models.Model):
    
    # USER_TYPE_CHOICES = (
    #     ('admin', 'Admin'),
    #     ('editor', 'Editor'),
    #     ('viewer', 'Viewer'),
    # )
    
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
   
   
    # user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    def __str__(self):
        return self.title
    
