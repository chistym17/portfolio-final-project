from django.shortcuts import get_object_or_404, redirect, render
from .models import Project, Rating
from .forms import RatingForm

def project_list(request):
    # if request.method == 'POST':
    #     project_id = request.POST.get('project_id')
    #     project = get_object_or_404(Project, pk=project_id)
    #     form = RatingForm(request.POST)
    #     if form.is_valid():
    #         rating = form.save(commit=False)
    #         rating.project = project
    #         rating.save()
    #         return redirect('projectlist')

    projects = Project.objects.all()
    form = RatingForm()
    
    return render(request, 'show_projects.html', {'projects': projects, 'form': form})
