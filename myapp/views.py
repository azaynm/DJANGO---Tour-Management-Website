from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TaskItem

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")

def viewPackages(request):
    return HttpResponse("View Pacages!")

def addPackage(request):
    return HttpResponse("Add Pacage!")


class ViewPackages(ListView):
    model = TaskItem
    template_name = 'myapp/view_packages.html'
