from django.db import models
from django.urls import reverse

class Experience(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.CharField(max_length=255, default='uncategorized')
    positioning = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.title #in the admin page see post

    def get_absolute_url(self):
        return reverse('cv_home')

class Category(models.Model):
    name = models.CharField(max_length=255)
    index = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name #in the admin page see post

    def get_absolute_url(self):
        return reverse('cv_home')
