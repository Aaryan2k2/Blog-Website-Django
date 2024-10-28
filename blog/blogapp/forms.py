from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User

class PostCreate(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']