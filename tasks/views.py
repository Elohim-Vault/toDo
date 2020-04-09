from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm


@login_required
def taskList(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        tarefas = Task.objects.filter(title__icontains=search, user=request.user)
    
    elif filter:
        tarefas = Task.objects.filter(done=filter, user=request.user)
    else:
        tarefas = Task.objects.all().order_by('-created_at').filter(user=request.user)
        paginator = Paginator(tarefas, 6)
        page = request.GET.get('page')
        tarefas = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tarefas': tarefas})


@login_required
def newTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtasks.html', {'form': form})


@login_required
def editTask(request, pk):
    tarefa = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=tarefa)
    if request.method == "POST":
        form = TaskForm(request.POST ,instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('detail-task', pk=pk)
    return render(request, 'tasks/edittask.html', {'form': form, 'tarefa': tarefa})


@login_required
def deleteTask(request, pk):
    tarefa = get_object_or_404(Task, pk=pk)
    tarefa.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')
    return redirect('task-list')


@login_required
def detailTask(request, pk):
    tarefa = get_object_or_404(Task, pk=pk)

    return render(request, 'tasks/detailTask.html', {'tarefa': tarefa})

@login_required
def changeStatus(request, pk):
    tarefa = get_object_or_404(Task, pk=pk)

    if tarefa.done == "doing":
        tarefa.done = "done"
    else:
        tarefa.done = "doing"

    tarefa.save()

    return redirect("/")

