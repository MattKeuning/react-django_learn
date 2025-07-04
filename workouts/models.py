from django.db import models

# Create your models here.

class Workout(models.Model):
    date = models.DateField()
    exercise = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return f'{self.date} - {self.exercise}'
    
class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.sets}x{self.reps})'