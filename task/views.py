from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Task


# Create your views here.

@login_required
def index(request):
    logged_in = request.user.id
    users = User.objects.all().exclude(id=logged_in)
    user_details = []
    for user in users:
        user_detail = dict()
        tasks = Task.objects.filter(task_user=user)
        task_name = ", ".join(str(task.task_name) for task in tasks)
        user_detail['id'] = user.id
        user_detail['name'] = user.username
        user_detail['task'] = task_name
        user_details.append(user_detail)
    return render(request, 'task/detail.html', {'users': user_details})

        
