from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.TextField(max_length=100)
    priority=models.IntegerField()
    date=models.DateField()
   
    
    def __str__(self) -> str:
        return self.task
    
    