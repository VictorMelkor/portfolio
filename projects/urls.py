from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.ListProjectsView.as_view(), name='projects'),
    path('new/', views.CreateProjectView.as_view(), name='new_project'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<int:pk>/update/', views.UpdateProjectView.as_view(), name='update_project'),
    path('<int:pk>/delete/', views.DeleteProjectView.as_view(), name='delete_project'),
]