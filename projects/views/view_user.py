from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from ..forms.user_forms import UserRegisterForm

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You are now able to log in.')
                return redirect('login')
        else:
            form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out ....")
    return render(request, 'users/logout.html', {})