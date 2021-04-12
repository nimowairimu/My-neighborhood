from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    profilephoto = CloudinaryField('profile photo')
    Bio = models.CharField(max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username


