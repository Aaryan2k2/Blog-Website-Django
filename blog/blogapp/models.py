from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now) #when the post is created then its time will be saved
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.username}--Post'
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    
    def __str__(self):
        return f'{self.author.username}--comment'
        