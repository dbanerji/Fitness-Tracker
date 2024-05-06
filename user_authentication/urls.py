from django.urls import path
from user_authentication import views

urlpatterns = [
    path('', views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
]