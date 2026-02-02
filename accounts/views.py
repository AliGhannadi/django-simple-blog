from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_view(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
  else:
      return redirect('/')
  return render(request, 'register.html', context)    

def login_view(request):
    if not request.user.is_authenticated:
     if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
             user = form.get_user()
             login(request, user)
             return redirect('/')
        else:
             messages.add_message(request,messages.ERROR,'Failed to login. username or password is incorrect.')     
     form = AuthenticationForm()
     context = {'form': form}
    else:
      return redirect('/')
    return render(request, 'login.html', context)

@login_required
def logout_view(request):
    if request.user.is_authenticated:
     logout(request)
    return redirect('/')