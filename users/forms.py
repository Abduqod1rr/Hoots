from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class cuserform(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password1','password2')

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "password1": forms.PasswordInput(attrs={"placeholder": "Password"}),
            "password2": forms.PasswordInput(attrs={"placeholder": "Repeat"}),
        }

        
        help_texts = {
            "username": "",              # chiqmaydi
            "password1": "create strong password",  # SENING yozuving chiqadi
            "password2": "repeat password",         # bu ham chiqadi
        }