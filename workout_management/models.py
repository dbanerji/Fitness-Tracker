from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError



class Exercise(models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField()
     muscle_group = models.CharField(max_length=100)
     def __str__(self):return self.name

class Workout(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     date = models.DateField()
     start_time = models.TimeField(default='06:00')
     end_time = models.TimeField(default='06:00')
     exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE,null=True)
     setnumber = models.TextField(default="1")
     number_of_reps = models.PositiveIntegerField(default=1)
     weight = models.DecimalField(max_digits=4,decimal_places=1,default=5.0)
     notes = models.TextField(blank=True)
     
     @property
     def duration_minutes(self):
        start = datetime.combine(self.date, self.start_time)
        end = datetime.combine(self.date, self.end_time)
        duration = end - start
        return duration.total_seconds() // 60
     
     def __str__(self):
            return f"{self.user.username}'s {self.exercise.name} Workout on {self.date}"

