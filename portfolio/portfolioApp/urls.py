from . import views
from django.urls import path, include

app_name = 'portfolioApp'
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', include([
        path('', views.about, name='about'),
        path('work-experience', views.work_experience, name='workExperience'),
        path('qualification', views.qualification, name='qualification'),
    ])),
    path('skills', views.skills, name='skills'),
    path('portfolio/', include([
        path('', views.portfolio, name='portfolio'),
        path('project/details/<int:id>', views.project_details, name='projectDetails')
    ])),
    path('testimonials', views.testimonials, name='testimonial'),
    path('blog/', include([
        path('', views.blog, name='blog'),
        path('post/topic/<int:id>', views.detailed_blog, name='detailedBlog'),
    ])),
    path('contact-me', views.contact_me, name='contactMe'),
    path('home', views.mobile_index, name='mobileHome'),
    path('blog/', include([
        path('posts', views.mobile_blog_posts, name='mobileBlog'),
        path('topic/<int:id>', views.mobile_individual_post, name='mobileIndividualBlog')
    ])),
    path('portfolio/', include([
        path('projects', views.mobile_portfolio, name='mobilePortfolio'),
        path('projects/project/details/<int:id>', views.mobile_individual_project, name='mobileProjectDetails')
    ])),
    path('about-me/', include([
        path('', views.mobile_about_me, name='mobileAboutMe'),
        path('work-experiences', views.mobile_work_experience, name='mobileWorkExperience'),
        path('qualifications', views.mobile_qualification, name='mobileQualifications')
    ])),
    path('skills-and-experiences', views.mobile_skills, name='mobileSkillsAndExperiences'),
    path('contact', views.mobile_contact_me, name='mobileContactMe')
]

