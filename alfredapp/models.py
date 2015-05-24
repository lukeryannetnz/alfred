from django.db import models
import RPi.GPIO as GPIO

class OnOffSwitch(models.Model):
	location = models.CharField(max_length=200)
	gpioPinBcmIndex = models.IntegerField(default=4)
	dateAddedUtc = models.DateTimeField('Date added')

	def toggle():
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)

		GPIO.setup(4, GPIO.OUT)
		GPIO.output(4, 1)

	def __str__(self):
		return self.location
