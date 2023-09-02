from django.db import models

class Resume(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to='resume/')
