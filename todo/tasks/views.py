from django.shortcuts import render
from .models import *


def tasks(request):
    all_tasks = Task.objects.all()
    context = {'all_tasks': all_tasks}
    return render(request, 'tasks/tasks.html', context)
