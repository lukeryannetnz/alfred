from django.test import TestCase
from .models import OnOffSwitch
from django.test.utils import setup_test_environment
from django.test import Client

setup_test_environment()

class OnOffSwitchTests(TestCase):

    def ignore_toggle_flips_state(self):
        """
        Ignored as these can only run on raspberry pi
        """
        sut = OnOffSwitch()
        initialstate = sut.get_state()

        sut.toggle_state()

        self.assertEqual(sut.get_state(), initialstate)
        sut.toggle_state()

class DeviceTests(TestCase):
    def test_device_get_all_200(self):
       client = Client()
       response = client.get("/api/devices/")
       self.assertEqual(response.status_code, 200)

    def test_device_get_all_empty(self):
        client = Client()
        response = client.get("/api/devices/")
        self.assertEqual(response.content, b'"[]"')

    def test_device_get_by_id_wrong_id_404(self):
        client = Client()
        response = client.get("/api/devices/45")
        self.assertEqual(response.status_code, 404)

    def test_device_get_by_id_200(self):
        self.createTestSwitch()
        client = Client()
        response = client.get("/api/devices/1")
        self.assertEqual(response.status_code, 200)

    def createTestSwitch(self):
        OnOffSwitch.objects.create(location="test switch", gpioPinBcmIndex=1)
