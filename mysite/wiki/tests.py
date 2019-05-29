from django.test import TestCase

from django.urls import reverse


class test_login:
   def login (self):
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "login")

def test_logout ():
# Create your tests here.
