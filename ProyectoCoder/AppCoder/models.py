from django.db import models

# Create your models here.
class Autor(models.Model):
    autor=models.CharField(max_length=40)
    info=models.CharField(max_length=40)
    orden=models.IntegerField()