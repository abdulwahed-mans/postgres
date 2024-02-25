from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or homepage
            return redirect('home')
        else:
            # Return an error message if authentication fails
            messages.error(request, 'Invalid username or password.')
    # Render the login page template
    return render(request, 'account/login.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or homepage
                return redirect('home')
        else:
            # Return an error message if the form is invalid
            messages.error(request, 'Invalid form submission. Please correct the errors.')
    else:
        form = UserCreationForm()
    # Render the signup page template with the signup form
    return render(request, 'account/signup.html', {'form': form})
