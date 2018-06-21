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
    path('testimonials', views.testimonials, name='testimonial')
]

