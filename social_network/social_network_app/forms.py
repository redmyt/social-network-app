from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'password1', 'password2', )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('sender', 'receiver', 'message_body', 'date')
