from django import forms
from django.contrib.auth import get_user_model
import re

User = get_user_model()


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter your name"

    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Enter your e-mail"
    }))
    contact = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Enter your message"
    }))

    def clean_name(self):
        name = self.cleaned_data.get("name")
        regex = re.compile("^[a-zA-Z]+$")
        if regex.match(name):
            return name
        else:
            raise forms.ValidationError("Name can contain only letters")


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already taken")
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already taken")
        else:
            return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Given passwords doesn't match")
        else:
            return data
