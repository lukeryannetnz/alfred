from django.db import models
import RPi.GPIO as GPIO
from datetime import datetime

class OnOffSwitch(models.Model):
	location = models.CharField(max_length=200)
	gpioPinBcmIndex = models.IntegerField(default=4)
	dateAddedUtc = models.DateTimeField('Date added', default=datetime.now)

	def toggle(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)

		GPIO.setup(self.gpioPinBcmIndex, GPIO.OUT)
		GPIO.output(self.gpioPinBcmIndex, not GPIO.input(self.gpioPinBcmIndex))

	def __str__(self):
		return self.location
