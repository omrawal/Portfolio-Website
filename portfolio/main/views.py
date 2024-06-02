from django.shortcuts import render, get_object_or_404
from .models import Project, Tag,Resume,ProfilePicture,Skill

# Create your views here.

def home(request):
    projects = Project.objects.all().order_by('rank')
    tags = Tag.objects.all()
    profile_picture = ProfilePicture.objects.all()[0]
    resume_file = Resume.objects.all()[0]
    skills = Skill.objects.all().order_by('rank')
    return render(request,'home.html',{'projects':projects,'tags':tags,'resume':resume_file,
                                       'profile_picture':profile_picture,
                                       'skills':skills,})

def contact(request):
    return render(request,'contact.html')

def project(request,id):
    project = get_object_or_404(Project,pk=id)
    return render(request,'project.html',{'project':project})
