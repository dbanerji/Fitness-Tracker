from django import forms

class SignupForm(forms.Form):
    full_name = forms.CharField(required=True,max_length=70)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True,min_length=5)
    confirm_password = forms.CharField(widget=forms.PasswordInput,required=True,min_length=5)

class LoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True, min_length=5)
    