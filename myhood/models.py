from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from cloudinary.models import CloudinaryField


# Create your models here.

class Neighbourhood(models.Model):
    hoodName = models.CharField(max_length=250)
    hoodLocation = models.CharField(max_length=250)
    photo =CloudinaryField('photo', default='photo')
    # admin = models.ForeignKey('User',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.hoodName} neighbourhood'


    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @property
    def occupants_count(self):
        return self.neighbourhood_users.count()


class UserManager(BaseUserManager):
    """
    Override User manager to restrict createsuperuser and createuser from prompting for neighbourhood
    """
    pass
    # def create_user(self, email, password=None):

    #     if email is None:
    #         raise TypeError('Users must have an email address.')

    #     user = self.model(email=self.normalize_email(email))
    #     user.set_password(password)
    #     user.save()

    #     return user

    # def create_superuser(self, email,username, password):

    #     if password is None:
    #         raise TypeError('Superusers must have a password.')
    #     user = self.create_user(username, password)
    #     user.is_superuser = True
    #     user.is_staff = True
    #     user.save()

    #     return user
    

class User(AbstractUser):
    neighbourhood = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE, related_name='neighbourhood_users', blank=True, null=True)
    # objects = UserManager()


class Profile (models.Model):
    name = models.CharField(max_length=30)
    idNo = models.IntegerField(default=0)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    emailaddress = models.CharField(max_length=50)
    status = models.BooleanField()
    photo =CloudinaryField('profile')
    user = models.OneToOneField(User,on_delete=models.CASCADE,default='')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save
    
    def delete_profile(self):
        self.delete()


class Business(models.Model):
    businessName = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    businessEmail = models.CharField(max_length=30)
    photo = CloudinaryField('businessphoto',default='')

    def __str__(self):

        return f'{self.businessName} business'

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    photo = CloudinaryField('postPhoto',default='',null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = '',null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE, default='', null=True, blank=True)


    def __str__(self):
        return f'{self.title} Post'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
    

