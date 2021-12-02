from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .models import Users
from  django import forms
class createuserform(UserCreationForm):
    class Meta:
        model=Users
        fields=['username','password']
 
class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"


class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)


