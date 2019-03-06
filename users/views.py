from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def new(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # added at 33 minute mark
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are able to login. {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/new.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')


def login(request):
    return render(request, 'users/login.html')




