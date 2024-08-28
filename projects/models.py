from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('new', 'New'),
    ('open', 'Open'),
    ('fixed', 'Fixed'),
    ('rejected', 'Rejected'),
    ('in_progress', 'In Progress'),
    ('closed', 'Closed'),
    ('test_passed', 'Test Passed'),
]

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    due_date = models.DateField(blank=True,null=True,default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True,null=True)
    role = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'
