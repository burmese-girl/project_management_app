from django.urls import path
from .views import view_projects, view_dashboard

urlpatterns = [
    path('projects', view_projects.ProjectListView.as_view(), name='project_list'),
    path('dashboard/', view_dashboard.dashboard, name='dashboard'),
    path('projects/<int:pk>/', view_projects.ProjectDetailView.as_view(), name='project_detail'),
]
