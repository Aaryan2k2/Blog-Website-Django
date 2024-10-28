from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            messages.success(request,f'Your Account has been created')
            user.save()
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,"registration/register.html",{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Profile has been updated!')
            return redirect('blog-home')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    return render(request,"profile.html",{'u_form':u_form,'p_form':p_form})