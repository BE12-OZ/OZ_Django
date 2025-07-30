from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Todo, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'
    paginate_by = 5

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'description', 'completed']
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todos:todo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todos/todo_detail.html'
    context_object_name = 'todo'

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['title', 'description', 'completed']
    template_name = 'todos/todo_form.html'
    
    def get_success_url(self):
        return reverse_lazy('todos:todo_detail', kwargs={'pk': self.object.pk})

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todos/todo_confirm_delete.html'
    success_url = reverse_lazy('todos:todo_list')
    context_object_name = 'todo'

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'todos/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.todo_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('todos:todo_detail', kwargs={'pk': self.kwargs['pk']})