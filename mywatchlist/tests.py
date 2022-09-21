from urllib import response
from django.test import TestCase

# Create your tests here.
class jsonTests(TestCase):
    def tests_testjsonpage(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
        
class xmlTests(TestCase):
    def tests_testxmlpage(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)
        
class htmlTests(TestCase):
    def tests_testhtmlpage(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)