from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Todo, Comment
from .forms import TodoForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string

class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todos/todo_list.html'
    context_object_name = 'todos'
    paginate_by = 5

    def get_queryset(self):
        return Todo.objects.filter(author=self.request.user)

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
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
    form_class = TodoForm
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
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.todo_id = self.kwargs['pk']
        comment = form.save()
        
        html = render_to_string('todos/partials/comment.html', {'comment': comment})
        return JsonResponse({'html': html})

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'todos/comment_update_form.html'

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('todos:todo_detail', kwargs={'pk': self.object.todo.pk})

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'status': 'ok'})
