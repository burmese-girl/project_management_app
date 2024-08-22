from django.shortcuts import render, redirect, get_object_or_404
from .models import Task,Project
from django.views.generic import ListView, DetailView

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def update_status(request, pk, status):
    task = get_object_or_404(Task, pk=pk)
    task.status = status
    task.save()
    return redirect('task_list')


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.task_set.all()
        return context