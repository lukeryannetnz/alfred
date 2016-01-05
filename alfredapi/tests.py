from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from django.core import serializers
from django.core.files.base import ContentFile

from .models import OnOffSwitch

class OnOffSwitchTests(TestCase):

    def ignore_toggle_flips_state(self):
        """
        Ignored (by not starting name with test_) as this can only run on raspberry pi
        """
        sut = OnOffSwitch()
        initialstate = sut.get_state()

        sut.toggle_state()

        self.assertEqual(sut.get_state(), initialstate)
        sut.toggle_state()

    def test_image_url_no_image(self):
        sut = OnOffSwitch()
        imageUrl = sut.image_url

        self.assertEqual('#', imageUrl)

    def test_image_url_with_image(self):
        sut = OnOffSwitch()
        sut.image.save('testimg.jpg', ContentFile('A string with the test file content'))
        imageUrl = sut.image_url

        self.assertTrue(imageUrl.startswith('/media/uploads'))
        self.assertTrue(imageUrl.find('testimg') > 0)

class DeviceApiTests(TestCase):
    def createTestSwitch(self):
        switch = OnOffSwitch.objects.create(location="test switch", gpioPinBcmIndex=15, description="test description")
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

        print(response)

    def test_single_item_content(self):
        switch = self.createTestSwitch()
        client = Client()
        response = client.get("/api/devices/")

        self.assertContains(response, switch.location)
        self.assertContains(response, switch.description)
        self.assertContains(response, switch.pk)

    def test_single_item_content_description(self):
        switch = OnOffSwitch.objects.create(location="test", description="test_description", gpioPinBcmIndex=1)

        client = Client()
        response = client.get("/api/devices/")

        self.assertContains(response, '"description": "test_description"')

    def test_single_item_image(self):
        switch = OnOffSwitch.objects.create(location="test", description="test_description", gpioPinBcmIndex=1)

        client = Client()
        response = client.get("/api/devices/")

        self.assertContains(response, '"image": "#"')

    def test_single_item_state(self):
        switch = self.createTestSwitch()

        client = Client()
        response = client.get("/api/devices/")
        self.assertContains(response, '"state": 0')

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

    def test_device_get_by_id_content(self):
        switch = self.createTestSwitch()
        client = Client()
        response = client.get("/api/devices/1")

        self.assertContains(response, switch.location)
        self.assertContains(response, switch.description)
        self.assertContains(response, switch.pk)

    def test_device_get_by_id_state(self):
        switch = self.createTestSwitch()

        client = Client()
        response = client.get("/api/devices/1")
        self.assertContains(response, '"state": 0')

    def test_device_get_by_id_image(self):
        switch = self.createTestSwitch()
        switch.image.save('imgfilename.jpg', ContentFile('A string with the test file content'))

        client = Client()
        response = client.get("/api/devices/1")
        self.assertContains(response, switch.image.url)

class DevicePatchByIdTests(DeviceApiTests):
    def test_device_patch_by_id_invalid_payload(self):
        switch = self.createTestSwitch()
        client = Client()
        response = client.patch("/api/devices/1", "invalid patch document")
        self.assertEqual(response.status_code, 400)

    def test_device_patch_by_id_toggle(self):
        switch = self.createTestSwitch()
        client = Client()
        response = client.patch("/api/devices/1", 'toggle')
        self.assertEqual(response.status_code, 200)
