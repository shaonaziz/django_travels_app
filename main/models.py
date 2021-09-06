from django.db import models


class Destination(models.Model):

    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)