from django.db import models

# Create your models here.
#Your new Phone Number is +19736015956
class Registration(models.Model):
	id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=50)
	Number = models.CharField(max_length=12)
	otp = models.CharField(max_length=6)

class Login(models.Model):
	Number = models.CharField(max_length=12)
	otp = models.CharField(max_length=6)


# import library 
import math, random 

def generateOTP() : 

	
	digits = "0123456789"
	OTP = "" 
	for i in range(4) : 
		OTP += digits[math.floor(random.random() * 10)] 

	return OTP 

if __name__ == "__main__" : 
	
	print("OTP of 4 digits:", generateOTP()) 
