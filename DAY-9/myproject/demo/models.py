from django.db import models


class Register(models.Model):
    first_name = models.CharField(max_length= 25)
    Last_name = models.CharField(max_length=25, null=True)
    email = models.EmailField(null=True)
    phone_num = models.CharField(max_length=10)
    age = models.IntegerField()

    gender_value = [('Male','Male'),('Female','Female')]
    gender = models.CharField(max_length=10,choices=gender_value)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.first_name