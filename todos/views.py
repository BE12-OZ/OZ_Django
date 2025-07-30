from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'description', 'completed']
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todos:todo_list')

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todos/todo_detail.html'
    context_object_name = 'todo'

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'description', 'completed']
    template_name = 'todos/todo_form.html'
    
    def get_success_url(self):
        return reverse_lazy('todos:todo_detail', kwargs={'pk': self.object.pk})

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todos:todo_list')
    context_object_name = 'todo'