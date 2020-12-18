from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=120)
    content=models.TextField()
    Last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title

class Userdata(models.Model):
    username=models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    followers= models.IntegerField()
    following= models.IntegerField()
    Last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.username