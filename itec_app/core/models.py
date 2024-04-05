from django.db import models

# Create your models here.
class Post(models.Model):
    titlu = models.CharField(max_length=255)
    continut = models.TextField(max_length=255)

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.username
    
