from django.db import models

class InterestedIn(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    popular = models.IntegerField(default=0)
    usersIn = models.IntegerField(default=0)
    suggestedTimes = models.IntegerField(default=0)
    display = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    imageUrl = models.ImageField(upload_to='interested/images', default='')
    iconUrl = models.ImageField(upload_to='interested/icons', default='')


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    imageUrl = models.ImageField(upload_to='post/images', default='')
