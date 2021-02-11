from django.db import models

# Create your models here.
class Registration(models.Model):
	id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=20)
	Number = models.CharField(max_length=12)
	otp = models.CharField(max_length=6)

class Login(models.Model):
	Number = models.CharField(max_length=12)
	otp = models.CharField(max_length=6)