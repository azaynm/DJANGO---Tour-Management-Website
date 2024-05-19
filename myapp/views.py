from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TaskItem
from django.urls import reverse_lazy
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")

class ViewPackages(ListView):
    model = TaskItem
    template_name = 'myapp/view_packages.html'
    context_object_name = 'packages'


class AddPackage(CreateView):
    model = TaskItem
    template_name = 'myapp/add_package.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('view_packages')


class UpdatePackage(UpdateView):
    model = TaskItem
    template_name = 'myapp/update_package.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('view_packages')


class DeletePackage(DeleteView):
    model = TaskItem
    template_name = 'myapp/delete_package.html'
    success_url = reverse_lazy('view_packages')