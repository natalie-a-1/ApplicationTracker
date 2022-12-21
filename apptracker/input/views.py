from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Application


def index(request):



class ApplicationListView(generic.ListView):
    model = Application
    context_object_name = 'application_list'  # your own name for the list as a template variable
    queryset = Application.objects.all()  # Get 5 books containing the title war
    template_name = 'application/application_list.html'
