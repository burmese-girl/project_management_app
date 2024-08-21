from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def update_status(request, pk, status):
    task = get_object_or_404(Task, pk=pk)
    task.status = status
    task.save()
    return redirect('task_list')
