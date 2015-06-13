from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from django.core import serializers

from .models import OnOffSwitch

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

class DeviceApiTests(TestCase):
    def createTestSwitch(self):
        switch = OnOffSwitch.objects.create(location="test switch", gpioPinBcmIndex=1)
        return switch

class DeviceGetAllTests(DeviceApiTests):
    def test_empty_200(self):
       client = Client()
       response = client.get("/api/devices/")
       self.assertEqual(response.status_code, 200)

    def test_empty_content(self):
        client = Client()
        response = client.get("/api/devices/")
        self.assertEqual(response.content.decode('UTF-8'), '{"items": []}')

    def test_single_item_200(self):
        self.createTestSwitch()
        client = Client()
        response = client.get("/api/devices/")
        self.assertEqual(response.status_code, 200)

    def test_single_item_content(self):
        switch = self.createTestSwitch()
        client = Client()
        response = client.get("/api/devices/")

        self.assertContains(response, switch.location)
        self.assertContains(response, switch.gpioPinBcmIndex)
        self.assertContains(response, switch.pk)

    def test_single_item_content_description(self):
        switch = OnOffSwitch.objects.create(location="test", description="test_description", gpioPinBcmIndex=1)

        client = Client()
        response = client.get("/api/devices/")

        self.assertContains(response, '"description": "test_description"')

    # def test_three_items_content(self):
    #     switch1 = self.createTestSwitch()
    #     switch2 = self.createTestSwitch()
    #     switch3 = self.createTestSwitch()
    #
    #     client = Client()
    #     response = client.get("/api/devices/")
    #
    #     expected = serializers.serialize('json', [switch1, switch2, switch3])
    #
    #     print(response.content)
    #
    #     for o in serializers.deserialize('json', response.content):
    #         print(o)
    #


        #self.assertEqual(response.content, expected)

class DeviceGetByIdTests(DeviceApiTests):

    def test_device_get_by_id_wrong_id_404(self):
        client = Client()
        response = client.get("/api/devices/45")
        self.assertEqual(response.status_code, 404)

    def test_device_get_by_id_200(self):
        self.createTestSwitch()
        client = Client()
        response = client.get("/api/devices/1")
        self.assertEqual(response.status_code, 200)

    def test_single_item_content(self):
        switch = self.createTestSwitch()
        client = Client()
        response = client.get("/api/devices/1")

        self.assertContains(response, switch.location)
        self.assertContains(response, switch.gpioPinBcmIndex)
        self.assertContains(response, switch.pk)
