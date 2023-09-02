from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    screenshots = models.ImageField(upload_to='project_screenshots/')
    technologies_used = models.CharField(max_length=255)
    project_url = models.URLField()

    def __str__(self):
        return self.title
