from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class category_name(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name

class blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(category_name,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    decription = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(blank=True,null=True)
    
    def __str__(self):
        return self.title
   