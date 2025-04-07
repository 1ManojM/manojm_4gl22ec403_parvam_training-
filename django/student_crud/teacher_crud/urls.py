from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name="teacher-list"),
    path('create', views.create_teacher, name="create-teacher"),
    path('view', views.view_teacher, name="view-teacher"),
    path('edit', views.view_teacher, name="edit-teacher"),
    path('delete', views.delete_teacher, name="delete-teacher"),
]