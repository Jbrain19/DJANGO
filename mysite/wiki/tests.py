from django.test import TestCase
from wiki.models import Page
from django.urls import reverse

#Testing the login works
class Test_login(TestCase):
        def testlogin(self):
                response = self.client.get(reverse('wiki:index'))
                self.assertContains(response, "Wiki Index") 

#Testing the logout function works
class Test_logout(TestCase):
        def testlogout(self):
                response = self.client.get(reverse('wiki:index'))
                self.assertContains(response, "logout") 


class Test_URL(TesCase):
        def  (self)
                 response = self.client.get(reverse('wiki:index'))
                self.assertContains(response, "") 



