from django.shortcuts import render,redirect
from django.http import Http404

from django.contrib.auth.models import User
from django.contrib import auth,messages
# Create your views here.
from .forms import SignupForm,LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    form = SignupForm(request.POST or None)
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
def login_user(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
    
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = email.split('@')[0]
            user = auth.authenticate(username=username,password=form.cleaned_data.get("password"))
            if user:
                auth.login(request,user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('workout_management:home')
            else:
                messages.error(request,'Invalid credentials')

        else:
            messages.error(request,'Invalid credentials')        
    else:
        if request.user.is_authenticated:
            return redirect('workout_management:home')
        form = LoginForm()
    return render(request,'user_authentication/login.html',{"form":form})

