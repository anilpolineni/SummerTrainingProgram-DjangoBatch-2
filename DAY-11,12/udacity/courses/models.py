from django.db import models

# Create your models here.

class Course(models.Model):
	course_name=models.CharField(max_length=50)
	image=models.CharField(max_length=500)
	description=models.TextField(max_length=1000)


	def __str__(self):
		return self.course_name


