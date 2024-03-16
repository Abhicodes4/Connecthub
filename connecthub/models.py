from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    postlocation=models.CharField(max_length=30)
    image=models.ImageField(upload_to='profile_pic1',null=True,blank=True)
    us=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.CharField(max_length=30)
    def __str__(self):
     return self.caption
     
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=50,default="hey there im using connecthub")
    profilepic=models.ImageField(upload_to='profile_pic1',null=True,blank=True,default='default2.png')
    def __str__(self):
     return str(self.user)


