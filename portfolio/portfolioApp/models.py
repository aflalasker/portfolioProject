from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Models for the Project and Project Details itself
class ProjectHeader(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    coverImage = models.ImageField()
    projectDetails = models.ForeignKey('ProjectDetails', on_delete=models.CASCADE)

    def __str__(self):
        return 'ID = {}, Title = {}'.format(self.id, self.title)


class ProjectDetails(models.Model):
    websiteLink = models.URLField(blank=True, null=True)
    projectLink = models.URLField(blank=True, null=True)
    detailedDescription = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.projectLink


# Model for Client Testimonials
class Testimonials(models.Model):
    clientCompanyName = models.CharField(max_length=50, blank=True, default='anonymous')
    clientName = models.CharField(max_length=50, blank=True, default='anonymous')
    testimonialDescription = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Company: {}, Client: {}'.format(self.clientCompanyName, self.clientName)


# Model for Resume
class Experience(models.Model):
    companyName = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField(blank=True, null=True)
    ifCurrentJob = models.CharField(max_length=25, blank=True, null=True)
    Description = models.TextField()  # Brief Description about the job you did

    def __str__(self):
        return self.companyName


class Qualification(models.Model):
    institution = models.CharField(max_length=50)
    graduatedDate = models.DateField(blank=True, null=True)
    subjects = models.TextField()  # For subjects and results
    overallGradesAndLevel = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.institution


class Skill(models.Model):
    name = models.CharField(max_length=50)
    skillImage = models.ImageField(blank=True, null=True)  # if the skill is HTML, upload an image of HTML logo

    def __str__(self):
        return self.name


class User(AbstractUser):
    title = models.CharField(max_length=20, blank=True, null=True)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    nickName = models.CharField(max_length=25)
    bio = models.TextField(blank=True, null=True)
    shortBio = models.TextField(blank=True, null=True)
    mobileNumber = models.IntegerField(blank=True, null=True)


class Blog(models.Model):
    blogTopic = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=50)
    dateCreated = models.DateField()

    def __str__(self):
        return self.blogTopic


class ContactMe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(blank=True, null=True)
    date_received = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Name: {}, Date Received: {}'.format(self.name, self.date_received)















