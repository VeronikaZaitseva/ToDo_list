from django.shortcuts import render, redirect, reverse
from .models import Task
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .forms import TodoForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})


def check(request, pk):
    current_task = Task.objects.get(id=pk)
    current_task.check = not current_task.check
    current_task.save()
    return redirect(reverse('index_url'))


def change_priority(request, pk):
    if request.method == 'POST':
        current_task = Task.objects.get(id=pk)
        form = TodoForm(request.POST, instance=current_task)
        current_task.priority = form['priority'].data
        current_task.save()
        return redirect(reverse('detail_url', kwargs={'pk': current_task.pk}))


class TaskCreate(CreateView):
    model = Task
    success_url = '/todo'
    template_name = 'create.html'
    form_class = TodoForm


class TaskDetail(DetailView):
    template_name = 'detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodoForm()
        return context


class TaskUpdate(UpdateView):
    template_name = 'update.html'
    model = Task
    success_url = '/todo'
    form_class = TodoForm


class TaskDelete(DeleteView):
    template_name = 'delete.html'
    model = Task
    success_url = '/todo'
