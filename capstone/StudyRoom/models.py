from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    CATEGORY_CHOICES = {
        'PR': "Private Room",
        'PU': "Public Room",
    }
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, related_name='rooms')
    description = models.TextField()
    members = models.ManyToManyField(User, related_name='members', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.name
    

class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title