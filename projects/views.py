from django.shortcuts import render
from projects.models import Project 

def projectIndex(request):
    projects = Project.objects.all() 
    context = {
        "projects": projects
    }
    return render(request, "projectIndex.html", context) 

def projectDetail(request, id):
    project = Project.objects.get(pk=id)
    context = {
        "project": project
    }
    return render(request, "projectDetail.html", context) 


