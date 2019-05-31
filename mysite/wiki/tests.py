from django.test import TestCase
from wiki.models import Page
from django.urls import reverse
from django.contrib.auth.models import User

# Testing the login works
class Test_login(TestCase):
    def testlogin(self):
        self.client.login(username='TestUser', password='TestUserPassword')
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "login")

# Testing the logout function works
class Test_logout(TestCase):
    def testlogout(self):
        self.client.logout()
        response = self.client.get(reverse('wiki:index'))
        self.assertContains(response, "logout")

# Testing the URL
class Test_URL(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('TestUser', 'TestUser@gmail.com', 'testingpassword')

        #../wiki/upload. This tests that the upload URL works
    def testuploadURL(self):
        response = self.client.get('/wiki/upload', follow=True)
        self.assertContains(response, "upload")

        #../wiki/page/edit. This tests that the edit URL works
    def testeditURL(self):
        self.client.login(username='TestUser', password='TestUserPassword')
        response = self.client.get('/wiki/editing/edit', follow=True)
        self.assertContains(response, "editing")

# testing 404 error
class Test_404(TestCase):
    def test404(self):
        response = self.client.get(reverse('wiki:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No pages available")
