from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import User, Skill, ProjectHeader, Testimonials, Experience, Qualification, Blog, ContactMe, AboutMe
from .forms import ContactMeForm

# Create your views here.


def index(request):
    user = User.objects.all()
    context = {'user': user}
    return render(request, 'portfolioApp/index.html', context)


def about(request):
    about_me_text = AboutMe.objects.all()
    context = {'about_me_text': about_me_text}
    return render(request, 'portfolioApp/about.html', context)


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


def blog(request):
    topics = Blog.objects.all()
    context = {'topics': topics}
    return render(request, 'portfolioApp/blog.html', context)


def detailed_blog(request, id):
    topic = get_object_or_404(Blog, id=id)
    context = {'topic': topic}
    return render(request, 'portfolioApp/detailedBlog.html', context)


def contact_me(request):
    form = ContactMeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "You message has been Successfully sent :)")
    context = {'form': form}
    return render(request, 'portfolioApp/contactMe.html', context)


def mobile_index(request):
    top_three_blog = Blog.objects.all().order_by('-id')[:3]
    context = {'top_three_blog': top_three_blog}
    return render(request, 'portfolioApp/mobileVersion/mobile_index.html', context)


def mobile_individual_post(request, id):
    post = get_object_or_404(Blog, id=id)
    context = {'post': post}
    return render(request, 'portfolioApp/mobileVersion/individual_post.html', context)


def mobile_blog_posts(request):
    mobile_blog = Blog.objects.all().order_by('-id')
    context = {'mobile_blog': mobile_blog}
    return render(request, 'portfolioApp/mobileVersion/mobile_blog_posts.html', context)


def mobile_portfolio(request):
    portfolio_mobile = ProjectHeader.objects.all().order_by('-id')
    context = {'portfolio': portfolio_mobile}
    return render(request, 'portfolioApp/mobileVersion/mobile_portfolio.html', context)


def mobile_individual_project(request, id):
    individual_project = get_object_or_404(ProjectHeader, id=id)
    context = {'pd': individual_project}
    return render(request, 'portfolioApp/mobileVersion/mobile_project_details.html', context)


def mobile_about_me(request):
    context = ''
    return render(request, 'portfolioApp/mobileVersion/mobile_about_me.html', {'context': context})


def mobile_work_experience(request):
    experience = Experience.objects.all().order_by('-id')
    context = {'experience': experience}
    return render(request, 'portfolioApp/mobileVersion/mobile_work_experiences.html', context)


def mobile_qualification(request):
    qualifications = Qualification.objects.all()
    context = {'qualification': qualifications}
    return render(request, 'portfolioApp/mobileVersion/mobile_qualification.html', context)


def mobile_skills(request):
    skills_and_experience = Skill.objects.all()
    context = {'skills': skills_and_experience}
    return render(request, 'portfolioApp/mobileVersion/mobile_skills_and_experiences.html', context)


def mobile_contact_me(request):
    form = ContactMeForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "You message has been Successfully sent :)")
    context = {'form': form}
    return render(request, 'portfolioApp/mobileVersion/mobile_contact_me.html', context)

