from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField( max_length=100)
    dec=models.TextField()
    img=models.ImageField(upload_to='static/images')
    price=models.FloatField()
    offer=models.BooleanField(default=False)
