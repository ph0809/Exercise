from django.db import models

# Create your models here.


"""创建一个新的Model"""
class Test(models.Model):
    name = models.CharField(max_length=20)
