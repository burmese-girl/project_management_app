from django.shortcuts import render
from ..models import Task

def dashboard(request):
    # Group tasks by status
    tasks_by_status = {
        'new': Task.objects.filter(status='new').count(),
        'in_progress': Task.objects.filter(status='in_progress').count(),
        'closed': Task.objects.filter(status='closed').count(),
        'fixed': Task.objects.filter(status='fixed').count(),
        'test_passed':Task.objects.filter(status='test_passed').count(),
    }

    return render(request, 'projects/dashboard.html', {'tasks_by_status': tasks_by_status})
