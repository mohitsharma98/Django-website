from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title