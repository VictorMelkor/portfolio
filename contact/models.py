from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.TextField(blank=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


