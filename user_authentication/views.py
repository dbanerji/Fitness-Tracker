from django.shortcuts import render
from django.http import Http404

from django.contrib.auth.models import User
# Create your views here.
from .forms import Signup

# Create your views here.
def signup(request):
    form = Signup(request.POST or None)
    if form.is_valid():
        password= form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")
        name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        if(password!= confirm_password):
            return render(request,'user_authentication/signup.html',{"form":form,"status":"Your passwords don't match!"})
        else:
            try:
                user = User.objects.get(email=email)
                return render(request,'user_authentication/signup.html',{"form":form,"status":"This email already exists in the system! Please log in instead."})
            except Exception as e:
                print(e)
                new_user = User.objects.create_user(username= name, email= email,password= password)
                new_user.save()
                return render(request,'user_authentication/signup.html',{"form":form,"status":"Signed up Successfully!"})
    return render(request,'user_authentication/signup.html',{"form":form})
def login(request):
    return render(request,'user_authentication/login.html')
def home(request):
    return render(request,'user_authentication/home.html')