from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        # We replaced the UserCreationForm with our costomize form which is UserRegisterForm
        form = UserRegisterForm(request.POST) # If we will input data to our register and actually create them
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # We are validating the data
            messages.success(request,f'Your account has been created! You can now log in.')
            return redirect('login') # This will return us to the homepage

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

"""
messages.debug
messages.info
messages.success
messages.warning
messages.error
"""