from django.db import models

# Create your models here.
class Todo(models.Model):
    name=models.TextField()
    priority=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name