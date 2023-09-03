
from django.shortcuts import render
from .models import Project
from django.db.models import Avg

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'show_projects.html', {'projects': projects})



