from . import views
from django.urls import path

app_name = 'portfolioApp'
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('skills', views.skills, name='skills')
]

