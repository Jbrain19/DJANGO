from django.db import models
from django.urls import reverse

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.title

    def get_absolute_url(self):
        return reverse('people.views.details', args=[str(self.id)])


class UserFileUpload (models.Model):
    upload = models.FileField(upload_to='uploads/')

    def _str_(self):
        return self.upload.name