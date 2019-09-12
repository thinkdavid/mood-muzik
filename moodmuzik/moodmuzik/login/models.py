from django.db import models

# Create your models here.
class User(models.Model):
	### FORMAT
	# COLUMN_NAME = MODELS.FIELD_INSTANCE(REQUIRED ARGUMENTS, OPTIONAL ARUGMENTS)
	name = models.CharField(max_length=200)
	last_login = models.DateTimeField('date logged in')

class Session(models.Model):
	activity = models.CharField(max_length=200)
	mood = models.CharField(max_length=200)
	weather = models.CharField(max_length=200)
	time_of_day = models.DateTimeField('date logged in')
	user = models.ForeignKey(User, on_delete=models.cascade)

class Song(models.Model):
	artist = models.CharField(max_length=200)
	tags = models.CharField(max_length=200)
	name = models.CharField(max_length=200)