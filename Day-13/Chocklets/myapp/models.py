from django.db import models

# Create your models here.


class User_register(models.Model):
	name=models.CharField(max_length=20)
	mailid=models.EmailField()
	phno=models.CharField(max_length=15)
	username=models.CharField(max_length=30,)
	password=models.CharField(max_length=30)
