from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from ..models import Task, Project

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def update_status(request, pk, status):
    task = get_object_or_404(Task, pk=pk)
    task.status = status
    task.save()
    return redirect('task_list')

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.task_set.all()
        return context

class ProjectUpdateView(LoginRequiredMixin, View):
    template_name = 'projects/project_update.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        return render(request, self.template_name, {'project': project})

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        project.name = request.POST.get('name')
        project.description = request.POST.get('description')
        project.start_date = request.POST.get('start_date')
        project.end_date = request.POST.get('end_date')
        project.save()
        return redirect('project_list')

