from django.shortcuts import render
from .models import Resume

def display_resumes(request):
    resume = Resume.objects.all()
    return render(request, 'show_resume.html', {'resume': resume[0]})
