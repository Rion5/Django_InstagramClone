from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def new(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # added at 33 minute mark
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('instagram-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/new.html', {'form': form})



