from django.db import models


# Create your models here.
class DemoModel(models.Model):
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=40)
    phone=models.IntegerField()
    email=models.EmailField()