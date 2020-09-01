from django.db import models

#class Author(models.Model):



class Audio(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    year = models.DateField()
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title

# Create your models here.
