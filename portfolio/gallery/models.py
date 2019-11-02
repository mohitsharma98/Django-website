from django.db import models

# Create your models here.
class Gallery(models.Model):
    image_title = models.TextField(max_length=200)
    image_des = models.TextField(max_length=500)
    image = models.FileField()

    def __str__(self):
        return self.image_title