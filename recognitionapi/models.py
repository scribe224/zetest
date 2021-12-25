from django.db import models

# Create your models here.

class Recognition(models.Model):
    status = models.CharField(max_length=32)
    text = models.TextField()
    #sourceimage = models.BinaryField()
