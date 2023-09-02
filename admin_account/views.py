from typing import Any
from django.shortcuts import render
from .models import Profile


from django.views.generic import FormView
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from portfolio.views import home


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

def show_profile(request):
    return render(request,'profile.html')

def loginPage(request):
    return render(request,'login.html')


class adminlog (LoginView):
    template_name='login.html'
    def get_success_url(self):
        return reverse_lazy('profile')              


class log_out(LogoutView):
    def get_next_page(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('loginPage')
    



@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    is_admin = request.user.is_staff  # Check if the user is an admin

    if is_admin and request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=user_profile) if is_admin else None

    return render(request, 'profile.html', {'user_profile': user_profile, 'form': form, 'is_admin': is_admin})
