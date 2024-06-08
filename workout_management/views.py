from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Workout
from .forms import WorkoutForm

@login_required
def home(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_management:workout_view')
    else:
        form = WorkoutForm()
    return render(request,'workout_management/home.html',{'form':form})

def workout_view(request):
    

    workouts = Workout.objects.filter(user=request.user)
    return render(request,'workout_management/workout_view.html',{"workouts":workouts})