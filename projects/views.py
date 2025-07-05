from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Rating

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def project_vote(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        score = int(request.POST.get('score'))
        Rating.objects.create(project=project, score=score)
        return redirect('projects:project_detail', pk=project.pk)
    return redirect('projects:project_list')