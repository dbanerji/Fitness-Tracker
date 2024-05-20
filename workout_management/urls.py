from django.urls import path
from .views import home

app_name = 'workout_management'

urlpatterns = [
    path('home/', home,name="home"),
]