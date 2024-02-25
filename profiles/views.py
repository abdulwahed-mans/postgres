# profiles/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile_detail')  
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile_edit.html', {'form': form})


@login_required 
def profile_detail(request, username): 
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile_detail.html', context)
    except Profile.DoesNotExist:
        messages.error(request, 'Profile not found.')
        return redirect('some-other-view')  
