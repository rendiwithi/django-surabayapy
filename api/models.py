from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    desc = models.TextField()
    img = models.ImageField()
    isOpen = models.BooleanField(blank=False, null=False)
    link = models.TextField()
    tema = models.CharField(max_length=100, blank=True, null=True)
    waktu = models.CharField(max_length=100, blank=True, null=True)
    tempat = models.CharField(max_length=100, blank=True, null=True)
    desc_closing = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
