from django.db import models

# Create your models here.
class IndexModel(models.Model):
    index_image1 = models.FileField()
    index_image2 = models.FileField()
    index_image3 = models.FileField()
    
    gmaillink = models.TextField()
    facebooklink = models.TextField()
    instagramlink = models.TextField()
    pinterestlink = models.TextField()
    
    model_image = models.FileField()
    
    aboutme = models.TextField(max_length=300)