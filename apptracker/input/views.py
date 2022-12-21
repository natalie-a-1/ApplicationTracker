from django.shortcuts import render

# Create your views here.
from .models import Application


def index(request):
    num_applications = Application.objects.all().count()
    context = {
        'Application': num_applications
    }
    return render(request, 'index.html', context=context)
