from django.urls import path
from .views import home,workout_view

app_name = 'workout_management'

urlpatterns = [
    path('home/', home,name="home"),
    path('workouts',workout_view,name="workout_view")
    
]