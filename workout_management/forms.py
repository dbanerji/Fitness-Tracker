from django import forms
from .models import Workout,Exercise

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date','start_time','end_time','exercise','setnumber', 'number_of_reps', 'weight', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time':forms.TimeInput(attrs={'type':'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'setnumber': forms.TextInput(attrs={'placeholder': 'e.g., Set 1'}),
            'number_of_reps': forms.NumberInput(attrs={'min': 1}),
            'weight': forms.NumberInput(attrs={'step': 0.1}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional notes...'}),
        }
    