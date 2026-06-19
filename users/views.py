from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterationForm

def register(request):
    if request.method == 'POST':
        form =UserRegisterationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

    else:
        form =UserRegisterationForm()

    return render(request, 'users/register.html', {'form': form})

