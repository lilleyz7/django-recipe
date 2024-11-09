from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .auth_forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            try:
                user.save()
                login(request, user)
                return redirect('Recipes:home')
            except Exception as e:
                return render(request, 'register.html', {'register_form': form, 'error_message': 'Unable to create user'})
        return render(request, 'register.html', {'register_form': form, 'error_message': 'Enter form correctly'})
    else:
        form = RegisterForm()
        return render(request,'register.html', {'register_form': form})

def login_user(request):
    if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/recipes/home')
            else:
                return render(request, 'login.html', {'login_form': form, 'error_message': 'Incorrect password'})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'login_form': form})
    
def user_logout(request):
    logout(request)
    return redirect('/authentication/login')