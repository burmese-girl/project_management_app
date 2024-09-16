from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .constants import STATUS_CHOICES, PROJECT_ROLES

class Project(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True,null=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    team_members = models.ManyToManyField('TeamMember', related_name='projects')

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    due_date = models.DateField(blank=True,null=True,default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    assignee = models.ForeignKey('TeamMember', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    role = models.CharField(max_length=100, choices = PROJECT_ROLES, default= 'staff')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='team_memberships')

    def __str__(self):
        return f'{self.user.username}-{self.role}'
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True, default='profile_pics/default.png')

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
