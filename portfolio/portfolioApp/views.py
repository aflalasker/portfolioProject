from django.shortcuts import render
from .models import User

# Create your views here.


def index(request):

    user = User.objects.all()

    context = {'user': user}

    return render(request, 'portfolioApp/index.html', context)


def about(request):
    user = User.objects.all()

    context = {'user': user}

    return render(request, 'portfolioApp/about.html', context)

