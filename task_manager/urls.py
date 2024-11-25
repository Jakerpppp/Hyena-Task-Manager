"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import handler404
import tasks.views as views

tasks = 'teams'
task_manager = 'teams'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('log_in/', views.LogInView.as_view(), name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('password/', views.PasswordView.as_view(), name='password'),
    path('profile/', views.ProfileUpdateView.as_view(), name='profile'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('create_team/', views.CreateTeamView.as_view(), name='create_team'),
    path('team/<int:team_id>', views.show_team, name='show_team'),
    path('team/<int:team_id>/invite/', views.invite, name='invite'),
    path('invitations/', views.list_invitations, name='list_invitations'),
    path('invitations/accept/<int:invitation_id>/', views.accept_invitation, name='accept_invitation'),
    path('invitations/decline/<int:invitation_id>/', views.decline_invitation, name='decline_invitation'),
    path('create_task/<int:team_id>', views.CreateTaskView.as_view(), name="create_task" ),
    path('team/edit_team/<int:team_id>', views.TeamUpdateView.as_view(), name='edit_team'),
    path('edit_task/<int:task_id>', views.EditTaskView.as_view(), name='edit_task'),
    path('delete_task/<int:task_id>', views.DeleteTaskView.as_view(), name = 'delete_task'),
    path('assign_member_to_task/<int:task_id>/<int:user_id>', views.assign_member_to_task, name= "assign_member_to_task"),
    path('notifications', views.notifications, name="notifications"),
    path('task_toggle/<int:task_id>', views.toggle_task_status, name='task_toggle'),
    path('toggle_archive/<int:task_id>', views.toggle_task_archive, name='toggle_archive'),
    path('leaderboard/<int:team_id>', views.leaderboard_view, name='leaderboard'),
    path('seen_notification/<int:notification_id>', views.seen_notification, name="seen_notification"),
    path('delete/<int:team_id>', views.DeleteTeamView.as_view(), name='team_delete'),
]

handler404 = 'tasks.views.custom_404'
