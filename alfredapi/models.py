''' Models for the alfred api '''
from django.db import models
import sys
from datetime import datetime

try:
    import RPi.GPIO as GPIO
except ImportError as e:
    print("Error occured importing RPi.GPIO. Are you running this code on a non-raspberry pi?")
    print(e)

class OnOffSwitch(models.Model):
    ''' An on off switch that can be toggled via GPIO. '''
    location = models.CharField(max_length=200)
    gpioPinBcmIndex = models.IntegerField(default=4)
    dateAddedUtc = models.DateTimeField('Date added', default=datetime.now)

    def toggle_state(self):
        ''' Toggles the state of the switch. Returns the current state. '''
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.gpioPinBcmIndex, GPIO.OUT)
        GPIO.output(self.gpioPinBcmIndex, not self.get_state())

        return self.get_state()

    def get_state(self):
        ''' Returns the current state of the switch '''
        return GPIO.input(self.gpioPinBcmIndex)

    def __str__(self):
        return self.location
