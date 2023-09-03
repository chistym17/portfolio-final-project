from django.db import models
from django.db.models import Avg

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    screenshots = models.ImageField(upload_to='project_screenshots/')
    technologies_used = models.CharField(max_length=255)
    project_url = models.URLField()
    ratings = models.ManyToManyField('Rating', related_name='projects', blank=True)

    def __str__(self):
        return self.title

    def average_rating(self):
        return self.ratings.aggregate(Avg('value'))['value__avg']

class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(choices=[(i, i) for i in range(8)])  

    def __str__(self):
        return str(self.value)
