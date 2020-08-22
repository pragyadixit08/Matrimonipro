from django.db import models

class RegisterData(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    GENDER_CHOICE =(
        ('Male','Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    mobile = models.BigIntegerField()
    dob = models.DateField()

class ContactData(models.Model):
    name = models.CharField(max_length=25)
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE)
    email = models.EmailField(max_length=30)
    mobile = models.BigIntegerField()
    about = models.CharField(max_length=2000)
