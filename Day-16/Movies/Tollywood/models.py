from django.db import models

# Create your models here.
class Tollywood(models.Model):
	moviename=models.CharField(max_length=30)
	heroname=models.CharField(max_length=30)
	heroinename=models.CharField(max_length=30)
	diretor=models.CharField(max_length=30)
	producer=models.CharField(max_length=30)
	cast=models.CharField(max_length=300)
	poster=models.ImageField()