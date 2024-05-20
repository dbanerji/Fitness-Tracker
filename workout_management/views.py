from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):

    #TODO workout logging system view needs to be redirected here
    
    return render(request,'workout_management/home.html')