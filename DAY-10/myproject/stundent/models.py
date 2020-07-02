from django.db import models


class SignUp(models.Model):
    name = models.CharField(max_length=50)
    roll_num = models.CharField(max_length=15,unique=True)
    gender_list = [('Male','Male'),('Female','Female')]
    gender = models.CharField(max_length=10,choices=gender_list)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name + self.roll_num
