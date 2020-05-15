from django.db import models

# A student model.


class Students(models.Model):

    firstname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    age = models.IntegerField()
    educationlevel = models.CharField(max_length=20)
