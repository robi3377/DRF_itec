from django.db import models

# Create your models here.
class Post(models.Model):
    titlu = models.CharField(max_length=255)
    continut = models.TextField(max_length=255)

class User():
    pass