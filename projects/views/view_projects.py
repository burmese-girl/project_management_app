from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
# from django.core.exceptions import PermissionDenied
from django.contrib import messages
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = User.objects.get(username=self.request.user.username)
        projects = self.get_queryset().filter(team_members__user=current_user)
        edit_permissions = []
        if projects != None:
            for i in projects:
                team_member = i.team_members.get(user=current_user)
                edit_permissions.append(team_member.is_admin() or team_member.is_manager())
        context['project_context'] = zip(projects, edit_permissions)
        return context

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.all()
        return context

class ProjectUpdateView(LoginRequiredMixin, View):
    template_name = 'projects/project_update.html'

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        current_user = self.request.user.username
        team_member = project.team_members.get(user=User.objects.get(username=current_user))
        admin_or_manager = team_member.is_admin() or team_member.is_manager()
        if admin_or_manager:
            pass
        else:
            # raise PermissionDenied("You do not have permission to access this page.")
            messages.warning(request, "You do not have permission to access this page.")
            return redirect('project_list')
        return render(request, self.template_name, {'project': project})

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        project.name = request.POST.get('name')
        project.description = request.POST.get('description')
        project.start_date = request.POST.get('start_date')
        project.end_date = request.POST.get('end_date')
        project.save()
        return redirect('project_list')

