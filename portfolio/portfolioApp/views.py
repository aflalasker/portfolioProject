from django.shortcuts import render, get_object_or_404
from .models import User, Skill, ProjectHeader

# Create your views here.


def index(request):
    user = User.objects.all()
    context = {'user': user}
    return render(request, 'portfolioApp/index.html', context)


def about(request):
    context = ' '
    return render(request, 'portfolioApp/about.html', {'context': context})


def skills(request):
    skill = Skill.objects.all()
    context = {'skill': skill}
    return render(request, 'portfolioApp/skills.html', context)


def portfolio(request):
    project = ProjectHeader.objects.all()
    context = {'project': project}
    return render(request, 'portfolioApp/portfolio.html', context)


def project_details(request, id):
    project = get_object_or_404(ProjectHeader, id=id)
    context = {'project': project}
    return render(request, 'portfolioApp/projectDetails.html', context)

