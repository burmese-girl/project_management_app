from django.urls import path
from .views import view_projects, view_dashboard

urlpatterns = [
    path('project_list', view_projects.ProjectListView.as_view(), name='project_list'),
    path('dashboard/', view_dashboard.dashboard, name='dashboard'),
    path('project_detail/<int:pk>/', view_projects.ProjectDetailView.as_view(), name='project_detail'),
    path('project_update/<int:pk>/', view_projects.ProjectUpdateView.as_view(), name='project_update'),
]
