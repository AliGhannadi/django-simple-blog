from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, UpdateUserInformation
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

@login_required
def profile_view(request):
    info_form = UpdateUserInformation(instance=request.user)
    pw_form = PasswordChangeForm(request.user)
    if request.method == 'POST':
      if 'update_info' in request.POST:
        info_form = UpdateUserInformation(request.POST,request.FILES,instance=request.user)
        if info_form.is_valid():
          info_form.save()
          messages.success(request, 'Profile Updated.', extra_tags='update_profile')
          return redirect('accounts:profile')
        else:
          messages.error(request, 'An error occured.', extra_tags='update_profile')
      elif 'update_pw' in request.POST:
        pw_form = PasswordChangeForm(request.user, request.POST)
        if pw_form.is_valid():
          user = pw_form.save()
          update_session_auth_hash(request, user)
          messages.success(request, 'Password successfully changed.', extra_tags='update_pw')
          return redirect('accounts:profile')
        else:
          messages.error(request, 'An error occured.', extra_tags='update_pw')
    context = {'pw_form': pw_form, 'info_form': info_form}
    return render(request, 'profile.html', context)
