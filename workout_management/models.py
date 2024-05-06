from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=100)

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField(default='06:00')
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE,null=True)
    setnumber = models.TextField(default="Set 1")
    numberOfReps = models.PositiveIntegerField(default=1)
    weight = models.DecimalField(max_digits=4,decimal_places=1,default=5.0)
    notes = models.TextField(blank=True)
    class Meta:
            ordering = ['-date', '-time']  # Ordering by date and time by default

    def clean(self):
            # Custom validation
        if self.number_of_reps <= 0:
            raise ValidationError("Number of reps must be a positive integer.")

    def save(self, *args, **kwargs):
            # Custom logic before saving
            # You can add more custom logic here if needed
        super().save(*args, **kwargs)

    def __str__(self):
            return f"{self.user.username}'s {self.exercise.name} Workout on {self.date}"

