from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=200,default='')
    address=models.CharField(max_length=300)
    pincode=models.CharField(max_length=300)
    city=models.CharField(max_length=300)
    state=models.CharField(max_length=300)
    country=models.CharField(max_length=300)


    def __str__(self):
        return self.user.username

