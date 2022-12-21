from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('applications/', views.ApplicationListView.as_view(), name='applications'),
]
