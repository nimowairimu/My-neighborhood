from .forms import profileForm,RegistrationForm,,UserUpdateForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import NeighbourHood, Profile
# from .forms import UpdateProfileForm, NeighbourHoodForm, PostForm
from django.contrib.auth.models import User


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        procForm=profileForm(request.POST, request.FILES)
        if form.is_valid() and procForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=procForm.save(commit=False)
            profile.user=user
            profile.save()

            # messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
        prof=profileForm()
    params={
        'form':form,
        'profForm': prof
    }
    return render(request, 'users/register.html', params)


def hoods(request):
    all_hoods = NeighbourHood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'all_hoods.html', params)

@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':

        userForm = UserUpdateForm(request.POST, instance=request.user)
        profile_form = profileForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('home')

    else:
        
        profile_form = profileForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        params = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'profile.html', params)


