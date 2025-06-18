from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Project
from . import forms

class ListProjectsView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    
    def get_queryset(self):
        qs = super().get_queryset()
        lang = self.request.GET.get('lang')
        order = self.request.GET.get('order', '-created_at')

        if lang: 
            qs = qs.filter(tech_stack__icontains=lang)

        if order in ['title', '-title', 'created_at', '-created_at']:
            qs = qs.order_by(order)
        else:
            qs = qs.order_by('title')

        return qs
    

class CreateProjectView(CreateView):
    model = Project
    form_class = forms.FormProject
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

class UpdateProjectView(UpdateView):
    model = Project
    form_class = forms.FormProject
    template_name = 'projects/update_project_form.html'
    success_url = reverse_lazy('projects')

class DeleteProjectView(DeleteView):
    model = Project
    template_name = 'projects/delete_project.html'
    success_url = reverse_lazy('projects:delete_confirmation')


