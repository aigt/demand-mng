from django.db import models


class Demand(models.Model):
    """Demand model class"""
    
    title = models.CharField(max_length = 150)
    text = models.TextField(blank = True)
    
    def __str__(self):
        return self.title
    

