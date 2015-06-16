''' Models for the alfred api '''
from django.db import models
from django.utils import timezone
from django.conf import settings
import sys
import os

try:
    import RPi.GPIO as GPIO
except Exception as e:
    print("Error occured importing RPi.GPIO. Are you running this code on a non-raspberry pi?")
    print(e)

class Device(models.Model):
    description =  models.CharField(max_length=200, default='')
    dateAddedUtc = models.DateTimeField('Date added', default=timezone.now)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    @property
    def image_url(self):
        """Gets the relative url for the image."""
        if self.image and hasattr(self.image, 'url'):
            return os.path.join(settings.MEDIA_URL ,self.image.url)
        else:
            return '#'

    class Meta:
        abstract = True

class OnOffSwitch(Device):
    ''' An on off switch that can be toggled via GPIO. '''
    gpioPinBcmIndex = models.IntegerField(default=4)

    ''' todo: move this to a constructor or __init__ function so it only gets run once'''
    def initialise_gpio(self):
        if 'GPIO' in globals():
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.gpioPinBcmIndex, GPIO.OUT)

    def toggle_state(self):
        ''' Toggles the state of the switch. Returns the current state. '''

        self.initialise_gpio()

        if 'GPIO' not in globals():
            print("RPi.GPIO not loaded. Can't toggle state.")
        else:
            GPIO.output(self.gpioPinBcmIndex, not self.get_state())

        return self.get_state()

    def get_state(self):
        ''' Returns the current state of the switch '''

        self.initialise_gpio()

        if 'GPIO' not in globals():
            print("RPi.GPIO not loaded. Can't load state. Returning 0 (off).")
            return 0;

        return GPIO.input(self.gpioPinBcmIndex)

    def __str__(self):
        return self.location
