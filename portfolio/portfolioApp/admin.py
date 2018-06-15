from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ProjectHeader, ProjectDetails, Testimonials, Experience, Qualification, Skill

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(ProjectHeader)
admin.site.register(ProjectDetails)
admin.site.register(Testimonials)
admin.site.register(Experience)
admin.site.register(Qualification)
admin.site.register(Skill)

