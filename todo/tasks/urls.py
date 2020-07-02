from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name="all_tasks"),
    path('update_task/<str:pk>/', views.update_task, name="update_task"),
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
]