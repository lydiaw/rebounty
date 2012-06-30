from django.db import models

ALERT_METHODS = (
	('text','text'),
	('call','call'),
	('email','email')
	)


CATEGORIES = (
	('furniture','furniture'),
	('electronics','electronics'),
	('food','food'),
	('tools','tools'),
	('cloting','clothing'),
	)

class User(models.Model):
    username = models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    

class Item(models.Model):
	user = models.ForeignKey(User)
	title = models.TextField()
	description = models.TextField()
	category = models.CharField(max_length=255, choices=CATEGORIES)
    

class Alerts(models.Model):
    query = models.CharField(max_length=200)
    method = models.CharField(max_length=200, choices=ALERT_METHODS)
    votes = models.IntegerField()