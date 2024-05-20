from django.urls import path
from user_authentication import views

app_name = 'authentication'

urlpatterns = [

    path('signup/',views.signup,name="signup"),
    path('login/',views.login_user,name="login"),
]