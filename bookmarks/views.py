from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bookmark

class BookmarkListView(LoginRequiredMixin, ListView):
    model = Bookmark
    template_name = 'bookmarks/bookmark_list.html'
    context_object_name = 'bookmarks'

    def get_queryset(self):
        return Bookmark.objects.filter(author=self.request.user)

class BookmarkDetailView(LoginRequiredMixin, DetailView):
    model = Bookmark
    template_name = 'bookmarks/bookmark_detail.html'
    context_object_name = 'bookmark'

    def get_queryset(self):
        return Bookmark.objects.filter(author=self.request.user)

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['name', 'url']
    template_name = 'bookmarks/bookmark_form.html'
    success_url = reverse_lazy('bookmarks:bookmark_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['name', 'url']
    template_name = 'bookmarks/bookmark_form.html'

    def get_queryset(self):
        return Bookmark.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('bookmarks:bookmark_detail', kwargs={'pk': self.object.pk})

class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    template_name = 'bookmarks/bookmark_confirm_delete.html'
    success_url = reverse_lazy('bookmarks:bookmark_list')
    context_object_name = 'bookmark'

    def get_queryset(self):
        return Bookmark.objects.filter(author=self.request.user)