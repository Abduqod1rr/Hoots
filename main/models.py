from django.db import models
from django.contrib.auth.models import User


class Hoots(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    title=models.CharField(max_length=20,default='no title')
    likes=models.ManyToManyField(User,null=True,blank=True,related_name='likes')
    hoot=models.FileField(upload_to='posts', null=True)
    posted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Following(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='followers')
    followed_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('user','follower')
        
    def __str__(self):
        return f"{self.follower.username} follows {self.user.username}"
