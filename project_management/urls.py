"""
URL configuration for project_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include, re_path
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from projects.views import view_projects, view_dashboard, view_user



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),

    path('projects/', include("projects.urls")),
    # path('', view_projects.ProjectListView.as_view(), name='project_list'),
    path('', view_dashboard.dashboard, name='dashbord'),

    path('register/', view_user.register, name='register'),
    path('login/', view_user.login_user.as_view(), name='login'),
    path('logout/', view_user.logout_user, name='logout'),

]
