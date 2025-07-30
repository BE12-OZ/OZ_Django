from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bookmark

def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    context = {'bookmarks': bookmarks}
    return render(request, 'bookmarks/bookmark_list.html', context)

def bookmark_detail(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    context = {'bookmark': bookmark}
    return render(request, 'bookmarks/bookmark_detail.html', context)

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['name', 'url']
    template_name = 'bookmarks/bookmark_form.html'
    success_url = reverse_lazy('bookmarks:bookmark_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)