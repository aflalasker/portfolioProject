from django.shortcuts import render, get_object_or_404
from .models import User, Skill, ProjectHeader, Testimonials, Experience, Qualification

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


def testimonials(request):
    testimonial = Testimonials.objects.all()
    context = {'testimonial': testimonial}
    return render(request, 'portfolioApp/testimonial.html', context)


def work_experience(request):
    experience = Experience.objects.all()
    context = {'experience': experience}
    return render(request, 'portfolioApp/workExperience.html', context)


def qualification(request):
    qualifications = Qualification.objects.all()
    context = {'qualification': qualifications}
    return render(request, 'portfolioApp/qualification.html', context)



