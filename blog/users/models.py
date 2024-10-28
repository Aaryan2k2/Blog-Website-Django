from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE) #made one to one field because eac user can have only one profile
    image=models.ImageField(blank=True,null=True,upload_to='profile-pics',default='images.jpg')

    def __str__(self):
        return f'{self.user.username}-Profile'
