from django.test import TestCase
from django.test import Client

# Create your tests here.
class HomePageTests(TestCase):

	def test_index_get_200(self):
		client = Client()
		response = client.get("/")

		self.assertEqual(response.status_code, 200)
