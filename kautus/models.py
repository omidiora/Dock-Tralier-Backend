from django.db import models
# Create your models here.
class DocksItem(models.Model):
    name = models.CharField(max_length=200)
    package_count = models.FloatField()
    countainer_count = models.FloatField()
    pause_count= models.FloatField()
    empty_trailzer= models.CharField(max_length=200)
    
